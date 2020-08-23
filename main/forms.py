from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from phone_field import PhoneFormField
from django.core.exceptions import ValidationError
from main.models import ModificatedUser, Record, Review
from .services import create_user_id
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from main.services import create_user_id

class AuthForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	username = forms.CharField(label="", widget=forms.EmailInput(
		attrs={"class": "form-control", "style": "width:17em;max-width:95%;align-self:center"}))
	password = forms.CharField(label="", widget=forms.PasswordInput(
		attrs={"class": "form-control", "style": "width:17em;max-width:95%;;align-self:center"}))


class RegForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;width:19em;max-width:100%;width:15em", "placeholder":"Логин"}))
	email = forms.EmailField(widget=forms.EmailInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":"E-mail"}))
	first_name = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em","placeholder":"Ваше имя"}))
	last_name = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":"Ваша фамилия"}))
	phone = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":"Номер телефона"}))
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":"Пароль"}))
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":"Подтверждение пароля"}))

	def clean_username(self):
		data = self.cleaned_data["username"]

		return data

	def clean_email(self):
		data = self.cleaned_data["email"]

		return data

	def clean_first_name(self):
		data = self.cleaned_data["first_name"]

		return data

	def clean_last_name(self):
		data = self.cleaned_data["last_name"]

		return data

	def clean_phone(self):
		data = self.cleaned_data["phone"]

		return data

	def clean_password1(self):
		data = self.cleaned_data["password1"]

		return data

	def clean_password2(self):
		data = self.cleaned_data["password2"]
		if data == self.cleaned_data["password1"]:

			return data

		raise ValidationError("Вашы пороли не совподают")


	def save(self):
	   
		user = User.objects.create(
			username=self.cleaned_data["username"],
			email=self.cleaned_data["email"],
			password=self.cleaned_data["password1"],
			last_name=self.cleaned_data["last_name"],
			first_name=self.cleaned_data["first_name"]
		)
		extended_info = ModificatedUser.objects.create(
			user=User.objects.get(
				username=self.cleaned_data["username"]
			),
			number=self.cleaned_data["phone"],
			number_of_user=create_user_id()
		)

		return user, extended_info


class RecordForm(forms.ModelForm):


	class Meta:
		model = Record
		fields = ("description","phone")
		labels = {
			"description": "Введите дополнительную информацию для врача",
			"phone": "Введите номер"}
		widgets = {
			"description": forms.Textarea(attrs={"class": "form-control", "style": "height:10em;resize:none", "placeholder": "Введите текст"}),
			"phone": forms.Textarea(attrs={"class": "form-control", "style": "height:4em;resize:none", "placeholder": "Пример: +380хххххххх"})
		}

	def clean_phone(self):

		data = self.cleaned_data["phone"]
		if data and not data.startswith("+"):
			raise ValidationError("It seems you haven't started your number with '+'")
		return data
		
	

	def check(self, request):
	
		self.request = request
		try:
			username = User.objects.get(username=self.request.user.username)
			if ModificatedUser.objects.filter(user=username) or self.request.POST.get("phone"):
				if Record.objects.filter(author=username, status=False, seen=False):
					return False
				return True   
			return False

		except ObjectDoesNotExist:
			
			if user_id := ModificatedUser.objects.filter(number_of_user=self.request.COOKIES["*1%"]):
				if Record.objects.filter(author=user_id.user.username,status=False):
					return False
				return True
			return False
			
		
	def save(self, *args, **kwargs) -> object:


		try:
			author = User.objects.get(username=self.request.user.username)
			
			try:
				ModificatedUser.objects.filter(user=author).update(made_records=True if F("made_records") is not True else False)
			
			except IntegrityError:
				ModificatedUser.objects.create(
					user = author,
					number_of_user = create_user_id(),
					made_records = True
				).save()

		except ObjectDoesNotExist:
			author = ModificatedUser.objects.select_related("user").get(number_of_user=self.request.COOKIES["*1%"]).user
			ModificatedUser.objects.filter(number_of_user=self.request.COOKIES["*1%"]).update(made_records=True if F("made_records") is not True else False)
		try:
			if more_info := ModificatedUser.objects.get(user=author).number:
				phone = more_info
			else:
				phone = self.cleaned_data["phone"]		
		except ObjectDoesNotExist:
			try:
				phone = ModificatedUser.objects.get(number_of_user=self.request.COOKIES["*1%"]).number
			except (ObjectDoesNotExist, KeyError):
				phone = self.cleaned_data["phone"]
		
		new_record = Record.objects.create(
			author=author.first_name,
			name=kwargs["service_name"],
			description=self.cleaned_data["description"],
			phone=phone)

		return new_record

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ("review", "mark")
		widgets = {
			"review": forms.Textarea(attrs={"class": "form-control","style":"height:8em;width:41.3em;margin-top:1.5em;max-width:100%;resize:none","placeholder":"Введите Ваш отзыв"}),
		}

	def save(self,*args,**kwargs):

		try:
			user = ModificatedUser.objects.select_related("user").get(number_of_user=kwargs["request"].COOKIES["*1%"]).user
		except KeyError:
			user = User.objects.get(username=kwargs["request"].user.username)

		new = Review.objects.create(
			author=user,
			review=self.cleaned_data["review"],
			mark=self.cleaned_data["mark"]
			)

		return new