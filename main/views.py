from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView,DeleteView
from django.views.generic.edit import FormView
from main.forms import AuthForm, RegForm, RecordForm, ReviewForm
from main.models import Service, Review, Record
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import add_message, ERROR, SUCCESS
from django.utils.translation import activate
import datetime
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
		context["todays_data"] = datetime.datetime.today().strftime("%Y-%m-%d")
		return context


class Info(TemplateView):
	"""Shows info page"""

	name = "Info"
	template_name = "main/info.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["work_time_bool"],context["work_time"] = get_work_date()[0],get_work_date()[1]
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

		return self.render_to_response(context={"form": AuthForm(request.GET)})

	def post(self, request, *args, **kwargs) -> object:

		# Gets username from form
		username = get_username_by_email(email=request.POST["username"])
		
		if username is None:
			return redirect("Account")

		# Gets User model instanse to other deeds
		
		user = authenticate(username=username,
							password=request.POST["password"])
		
		# Checks whether user is admin to permanent authentification
		if check_admin(username):
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect("Account")

		# Checks whether user pressed ratio button and login him
		
		if request.POST.get("check"):
			if user:
				login(request, user, backend='django.contrib.auth.backends.ModelBackend')
				return redirect("Account")
			return redirect("Account")

		# Gets user id by username stated in form
		user_id = get_user_id_by_username(username=username)
		
		# Validates user's id to futher authentification
		if user_id:
			response = redirect("Account")

			# Writes some cookie to futher checking of credentials
			response.set_cookie("*1%", user_id, expires=6000)
			return response

		# Writes error message if user is not regestrated
		# and redirects to the Account page
		add_message(self.request, ERROR, "Вы не зарегестрированы")
		return redirect("Account")


class Regestration(FormView):
	"""Releases regestration functionality"""

	name = "Reg"
	template_name = "main/reg.html"
	form_class = RegForm
	success_url = reverse_lazy("Account")

	def form_valid(self,form) -> object:
		if form.is_valid():
			form.save()
			add_message(self.request, SUCCESS, "Поздравляю!Ви зарегестрированы ")
			return super().form_valid(form)
	
	def form_invalid(self, form):
		for error_field_name in form.errors:
			add_message(self.request, ERROR, form.errors[error_field_name].as_text)
		return super().form_invalid(form)



class ServiceList(ListView):
	"""Shows us Service List page"""

	name = "Services"
	template_name = "main/services.html"
	context_object_name = "services"

	def get_queryset(self) -> object:
		splited_query = SplitedQuerySet()
		queryset = splited_query.get_list(model=Service)
		return queryset

	


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
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().post(request, *args, **kwargs)
		

	def form_valid(self, form):
		
		if form.is_valid():
			if form.check(self.request):
				form.save(service_name=self.request.POST["service_name"])

				add_message(self.request, SUCCESS,
							"Вы успешно были записаны")
				
				return super().form_valid(form)
			add_message(self.request, ERROR,
						"Произошла ошибка")
			return super().form_invalid(form)


	def form_invalid(self, form):
		for error_field_name in form.errors:
			add_message(self.request, ERROR, form.errors[error_field_name])
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


def set_language(request, language_code):
	"""Sets a language of user's interface"""

	activate(language_code)
	if previous_path := request.session.get("previous_path"):
		if previous_path == "%(code)s/set_language/%(code)s" % {"code": language_code}:
			return redirect("Landing")
		return HttpResponseRedirect("/%s/%s" % (language_code, request.session["previous_path"]))
	return redirect("Landing")


def mailinglist_subscribing(request):
	pass