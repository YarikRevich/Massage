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
from main.decorators import is_authenticated
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from main.validators import PasswordValidator
from django.utils.translation import gettext_lazy as _


class PasswordChangeForm(SetPasswordForm):
	"""Form for the password changing"""


	new_password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"form-control", "style":"width:20em;max-width:96%", "placeholder":"Новый пароль"}))
	new_password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"form-control", "style":"width:20em;margin-top:1em;margin-bottom:1em;max-width:96%", "placeholder":"Подтверждение пароля"}))


	def clean_new_password1(self):
		"""Cleans password1"""

		password1 = self.cleaned_data["new_password1"]
		validator = PasswordValidator(password1, self.user)
		validated_data = validator.validate()
		if not validated_data[0]:
			raise ValidationError(validated_data[1])
		return password1
	

	def clean_new_password2(self):
		"""Cleans password2"""

		password1 = self.cleaned_data.get("new_password1")
		password2 = self.cleaned_data.get("new_password2")
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError(
					_("Пароли не совпадают!")
				)
		return password2


class PasswordResetForm(PasswordResetForm):
	"""Form to pass an email for the futher pass-reset"""

	email = forms.CharField(
		label="", 
		widget=forms.EmailInput(attrs={"class":"form-control", "style": "width:20em;margin-top:1em;margin-bottom:1.2em;max-width:95%;align-self:center","placeholder":_("Ваш E-mail")}))


class AuthForm(AuthenticationForm):
	"""Form for the authentification"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	username = forms.CharField(label="", widget=forms.EmailInput(
		attrs={"class": "form-control", "style": "width:17em;margin-top:1em;max-width:95%;align-self:center","placeholder":_("Ваш E-mail")}))
	password = forms.CharField(label="", widget=forms.PasswordInput(
		attrs={"class": "form-control", "style": "width:17em;margin-top:1em;max-width:95%;;align-self:center","placeholder":_("Пароль")}))


class RegForm(forms.Form):
	"""Form for the registartions"""

	username = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;width:19em;max-width:100%;width:15em", "placeholder":_("Логин")}))
	email = forms.EmailField(widget=forms.EmailInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":"E-mail"}))
	first_name = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em","placeholder":_("Ваше имя")}))
	last_name = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":_("Ваша фамилия")}))
	phone = forms.CharField(widget=forms.TextInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":_("Номер телефона")}))
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":_("Пароль")}))
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={"class": "form-control", "style": "margin-top:1em;max-width:100%;width:15em", "placeholder":_("Подтверждение пароля")}))


	def clean_username(self):
		"""Cleans username"""

		data = self.cleaned_data["username"]
		if User.objects.filter(username=data).exists():
			raise ValidationError(_("Пользователь с таким логином уже существует"))
		return data


	def clean_email(self):
		"""Cleans username"""

		data = self.cleaned_data["email"]
		if User.objects.filter(email=data).exists():
			raise ValidationError(_("Пользователь с таким E-mail уже существует"))
		return data


	def clean_first_name(self):
		"""Cleans first_name"""

		data = self.cleaned_data["first_name"]
		return data


	def clean_last_name(self):
		"""Cleans last_name"""

		data = self.cleaned_data["last_name"]
		return data


	def clean_phone(self):
		"""Cleans phone"""

		data = self.cleaned_data["phone"]
		return data


	def clean_password1(self):
		"""Cleans password1"""

		data = self.cleaned_data["password1"]
		return data


	def clean_password2(self):
		"""Cleans password2"""

		data = self.cleaned_data["password2"]
		if data == self.cleaned_data["password1"]:
			return data
		raise ValidationError(_("Вашы пороли не совподают"))


	def save(self):
		"""Creates a new entry"""
		
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
	"""Form for the record making"""

	class Meta:
		model = Record
		fields = ("description","phone")
		labels = {
			"description": _("Введите дополнительную информацию для врача"),
			"phone": _("Введите номер")}
		widgets = {
			"description": forms.Textarea(attrs={"class": "form-control", "style": "height:10em;resize:none", "placeholder": _("Введите текст")}),
			"phone": forms.TextInput(attrs={"class": "form-control", "style": "height:4em;resize:none", "placeholder": _("Пример: +380хххххххх")})
		}


	def clean_phone(self):
		"""Cleans phone"""

		data = self.cleaned_data["phone"]
		if data:
			if not data.startswith("+") and not data == "__":
				raise ValidationError(_("Кажеться что Вы написали номер без '+' в начале"))	
			return data
		raise ValidationError(_("Кажеться, что Вы не написали номер телефона"))
		
	
	def check(self, request):
		"""Checks whether user has already made any records"""

		self.request = request
		try:
			user = ModificatedUser.objects.select_related("user").get(number_of_user=self.request.COOKIES["*1%"]).user
		except (ObjectDoesNotExist, KeyError):
			try:
				user = User.objects.get(username=self.request.user.username)
			except:
				return (False, _("Пользователь с таким именем не найден"))

		if ModificatedUser.objects.filter(user=user) or self.request.POST.get("phone"):
			if Record.objects.filter(author=user.first_name, status=False, seen=False):
				return (False, _("Вы уже сделали запись на сеанс. Для того чтобы записаться нужно отменить запись на предыдущий в 'Карточке клиента'"))
			return (True, _("Поздравляю! Вы были записаны"))  
		return (False, _("Произошла ошибка, попробуйте снова через несколько минут"))

		
	def save(self, *args, **kwargs) -> object:
		"""Creates a new entry"""

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
			if user_phone := ModificatedUser.objects.get(user=author).number:
				phone = user_phone
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
	"""Form for the leaving reviews"""

	class Meta:
		model = Review
		fields = ("review", "mark")
		widgets = {
			"review": forms.Textarea(attrs={"class": "form-control","style":"height:8em;width:41.3em;margin-top:1.5em;max-width:97.5%;resize:none","placeholder":_("Введите Ваш отзыв")}),
		}


	@is_authenticated
	def save(self,request,*args,**kwargs):
		"""Creates a new entry"""
		
		try:
			user = ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user
		except (ObjectDoesNotExist, KeyError):
			user = User.objects.get(username=request.user.username)

		new = Review.objects.create(
			author=user,
			review=self.cleaned_data["review"],
			mark=self.cleaned_data["mark"]
			)

		return new