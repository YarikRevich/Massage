import datetime
import Massage.settings
from social_django.models import UserSocialAuth
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView,DeleteView
from django.views.generic.edit import FormView, View
from main.forms import AuthForm, RegForm, RecordForm, ReviewForm, PasswordResetForm, PasswordChangeForm
from main.models import Service, Review, Record
from django.contrib.auth.views import PasswordResetConfirmView
from django.http import JsonResponse
from django.contrib.auth import login, logout
from main.authentication_backend import authentication
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import add_message, ERROR, SUCCESS, INFO
from django.utils.translation import activate
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from main.validators import LoginUserValidator
from django.utils.translation import gettext_lazy as _
from main.services import (get_username_by_email,
						check_admin,
						made_records,
						get_all_made_orders,
						create_user_id,
						get_user_id_by_username,
						get_first_name,
						get_users_records,
						get_last_name,
						get_email,
						get_user,
						get_user_phone_number,
						get_work_date,
						get_all_reviews,
						get_all_records,
						get_user_data,
						get_newest_services,
						get_first_service,
						get_service_info,
						get_info_about_doctor,
						get_all_visit_images,
						get_first_visit_image,
						do_logout__cookie,
						get_all_auth_service_status,
						SplitedQuerySet)


class Landing(TemplateView):
	"""Shows main landing page"""

	name="Landing"
	template_name = "main/landingpage.html"

	def get_context_data(self, **kwargs) -> dict:
		context = super().get_context_data(**kwargs)
		context["order_count"] = get_all_made_orders()
		context["first_service"] = get_first_service()
		context["newest_services"] = get_newest_services()
		context["language_code"] = self.request.LANGUAGE_CODE
		context["todays_data"] = datetime.datetime.today().strftime("%Y-%m-%d")
		context["info_about_doctor"] = get_info_about_doctor(self.request)
		context["visit_images"] = get_all_visit_images()
		context["first_visit_image"] = get_first_visit_image()
		return context


class Info(TemplateView):
	"""Shows info page"""

	name = "Info"
	template_name = "main/info.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["work_time_bool"],context["work_time"] = get_work_date()[0],get_work_date()[1]
		context["lang_code"] = self.request.LANGUAGE_CODE
		return context
	

class Account(TemplateView):
	"""Releases account page and login functionality"""

	name = "Account"
	template_name = "main/account.html"

	def get(self, request, *args, **kwargs) -> object:

		# Checks if user is authentifiacated or has cookies user_id for the authentification
		if request.user.is_authenticated or request.COOKIES.get("*1%"):
			context = {
				"form": None,
				"user_data": get_user_data(request),
				"records": get_users_records(request),
				"made_records": made_records(request)
			}
			return self.render_to_response(context=context)

		return self.render_to_response(context={"form": AuthForm(request.GET), "auth_services": get_all_auth_service_status()})

	def post(self, request, *args, **kwargs) -> object:

		# Gets username from form
		username = get_username_by_email(email=request.POST["username"])
		if username:
			validator = LoginUserValidator(username)
			if request.POST.get("check"):
				if validated_user := validator.validate_user__check_on(request):
					login(request, validated_user, backend='django.contrib.auth.backends.ModelBackend')
					add_message(request, SUCCESS, _("Вы вошли в аккаунт!"))
					return redirect("Account")
				add_message(request, ERROR, _("Данные пользователя введены не правильно"))
				return redirect("Account")
			else:
				if validated_user := validator.validate_user__check_off():
					if isinstance(validated_user, int):
						add_message(request, SUCCESS, _("Вы вошли в аккаунт!"))
						response = redirect("Account")
						response.set_cookie("*1%", validated_user)
						return response
					login(request, validated_user, backend='django.contrib.auth.backends.ModelBackend')
					add_message(request, SUCCESS, _("Вы вошли в аккаунт!"))
					return redirect("Account")
				add_message(request, ERROR, _("Данные пользователя введены не правильно"))
				return redirect("Account")
		add_message(request, ERROR, _("Вы не указали E-mail"))
		return redirect("Account")


class Regestration(FormView):
	"""Releases regestration functionality"""

	name = "Reg"
	template_name = "main/reg.html"
	form_class = RegForm
	success_url = reverse_lazy("Account")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["auth_services"] = get_all_auth_service_status()
		return context

	def form_valid(self,form) -> object:
		if form.is_valid():
			form.save()
			add_message(self.request, SUCCESS, "Поздравляю!Ви зарегестрированы ")
			return super().form_valid(form)
	
	def form_invalid(self, form):
		for error_field_name in form.errors:
			add_message(self.request, ERROR, form.errors[error_field_name].as_text())
		return super().form_invalid(form)


class ServiceList(ListView):
	"""Shows us Service List page"""

	name = "Services"
	template_name = "main/services.html"
	context_object_name = "services"

	def get_queryset(self) -> object:
		splited_query = SplitedQuerySet()
		queryset = splited_query.get_list(model=Service, category=self.kwargs["filter"])
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["language_code"] = self.request.LANGUAGE_CODE
		return context

	def post(self, request, *args, **kwargs):
		return redirect("Services", filter=request.POST["filter"])		
	

class ServiceInfo(DetailView, FormView):
	"""Shows us page with more detailed info about equal service"""

	name = "ServiceInfo"
	template_name = "main/serviceinfo.html"
	context_object_name = "service"
	model = Service
	form_class = RecordForm

	def get_success_url(self) -> str:

		self.success_url = reverse_lazy("ServiceInfo", kwargs={"pk": self.kwargs["pk"]})
		return self.success_url

	def get_context_data(self, **kwargs) -> dict:

		context = super().get_context_data(**kwargs)
		try:
			context["authed"] = self.request.COOKIES["*1%"]
		except KeyError:
			try:
				context["authed"] = self.request.user.username
			except KeyError:
				context["authed"] = False
		context["has_number"] = get_user_phone_number(self.request)
		context["service_info"] = get_service_info(self.kwargs["pk"])
		context["language_code"] = self.request.LANGUAGE_CODE
		if self.request.get_full_path() != "/{}/{}".format(self.request.LANGUAGE_CODE, self.request.session.get("previous_path")):
			context["previous_page"] = "/{}/{}".format(self.request.LANGUAGE_CODE, self.request.session.get("previous_path"))
			context["previous_page_status"] = True
		else:
			context["previous_page"] = "/{}/home/services/".format(self.request.LANGUAGE_CODE)
			context["previous_page_status"] = False
		return context

	def post(self, request, *args, **kwargs):

		self.object = self.get_object()
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		
		ckecking_result = form.check(self.request)
		if ckecking_result[0]:
			form.save(service_name=self.request.POST["service_name"])

			add_message(self.request, SUCCESS,
					ckecking_result[1])
			return super().form_valid(form)

		add_message(self.request, ERROR,
					ckecking_result[1])
		return super().form_invalid(form)

	def form_invalid(self, form):

		for error_field_name in form.errors:
			add_message(self.request, ERROR, form.errors[error_field_name].as_text())
		return super().form_invalid(form)


class ReviewPage(FormView, ListView):
	"""Shows review page"""

	name = "Reviews"
	paginate_by = 4
	model = Review
	template_name = "main/review.html"
	form_class = ReviewForm
	success_url = reverse_lazy("Reviews", kwargs={"page": 1})


	def get_context_data(self, **kwargs) -> dict:
		context = super().get_context_data(**kwargs)
		context["reviews"] = get_all_reviews()
		context["user_is_author"] = get_user(self.request)
		return context


	def form_valid(self,form) -> object:
		if form.is_valid():
			form.save(self.request)
			return super().form_valid(form)
		return super().form_invalid(form)


class DeleteReviewClass(DeleteView):
	"""Deletes review"""

	name="DeleteReviews"
	queryset = get_all_reviews()
	success_url = reverse_lazy("Reviews", kwargs={"page":1})

	def get(self,request,*args, **kwargs):
		return super().post(request,*args,**kwargs)


class DeleteRecordClass(DeleteView):
	"""Deletes record"""

	name = "DeleteRecord"
	queryset = get_all_records()
	success_url = reverse_lazy("Account")

	def get(self,request,*args, **kwargs):
		return super().post(request,*args,**kwargs)


class PasswordReset(View):

	name = "PasswordReset"

	def get(self, request, *args, **kwargs) -> object:

		context = {"form": PasswordResetForm()}
		return render(request, "main/reset_password.html", context)

	def post(self, request, *args, **kwargs) -> object:
		
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data["email"]
			if (data := User.objects.filter(email=email)) and not UserSocialAuth.objects.filter(uid=email):
				for user in data:
					subject = "Востановление пароля Emassage.name"
					template = "main/reset_password__email.html"
					context = {
						"domain": Massage.settings.DOMAIN,
						"protocol":"http",
						"uid":urlsafe_base64_encode(force_bytes(user.pk)),
						"token": default_token_generator.make_token(user),
						"user":user,
						"email":user.email,
						"site_name":"Emassage.name",
					}
					email = get_template(template).render(context)
					send_mail(subject=subject, message=None, from_email=Massage.settings.EMAIL_HOST_USER, recipient_list=[user.email], html_message=email, fail_silently=True)
				
				add_message(request, INFO, "Вам было отправлено письмо на почту, проверте её!")
				return redirect("PasswordReset")
			if UserSocialAuth.objects.filter(uid=email):
				add_message(request, ERROR, "Пользователь с таким E-mail зарегестрирован через соц.сеть. Поэтому пароль не может быть изменён")
			else:
				add_message(request, ERROR, "Пользователя с таким E-mail не существует")
			return redirect("PasswordReset")
		add_message(request, ERROR, "Что-то пошло не так. Попробуйте снова")
		return redirect("PasswordReset")


class PasswordResetConfirm(PasswordResetConfirmView):

	name = "PassResetConfirm"
	template_name = "main/password_reset_confirm.html"
	form_class = PasswordChangeForm
	success_url = reverse_lazy("Landing")

	def form_invalid(self, form):
		try:
			add_message(self.request, ERROR, form.errors["new_password1"].as_text())
		except KeyError:
			add_message(self.request, ERROR, form.errors["new_password2"].as_text())
		return redirect("PassResetConfirm", uidb64=self.kwargs["uidb64"], token=self.kwargs["token"])


def logout_user(request: object) -> object:
	"""Does logout mechanism"""

	if do_logout__cookie(request):
		response = redirect("Landing")
		response.delete_cookie("*1%")
		return response
	logout(request)
	return redirect("Landing")


def set_language(request: object, language_code: str) -> object:
	"""Sets a language of user's interface"""

	activate(language_code)
	if previous_path := request.session.get("previous_path"):
		if previous_path == request.get_full_path():
			return redirect("Landing")
		return HttpResponseRedirect("/%s/%s" % (language_code, request.session["previous_path"]))
	return redirect("Landing")


def mailinglist_subscribing(request: object):
	"""Subscribes user on mailinglist"""

	add_message(request, INFO, "Данная функция находиться в розработке")
	if previous_path := request.session.get("previous_path"):
		if previous_path == request.get_full_path():
			return redirect("Landing")
		return HttpResponseRedirect("/%s/%s" % (request.LANGUAGE_CODE, request.session["previous_path"]))
	return redirect("Landing")