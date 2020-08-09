from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main.forms import AuthForm, RegForm, RecordForm, ReviewForm
from main.models import Service, Review
from django.http import JsonResponse
from main.services import get_username_by_email, check_admin, get_all_made_orders, create_user_id, get_user_id_by_username, get_first_name, get_last_name, get_email, get_user, SplitedQuerySet
from django.contrib.auth import authenticate, login
from django.contrib.messages import add_message, ERROR, SUCCESS


class Landing(TemplateView):
    """Shows main landing page"""

    template_name = "main/landingpage.html"

    def get_context_data(self, **kwargs):
        contenxt = super().get_context_data(**kwargs)
        contenxt["order_count"] = get_all_made_orders()


class Info(TemplateView):
    """Shows info page"""

    template_name = "main/info.html"


class Account(TemplateView):
    """Releases account page and login functionality"""

    template_name = "main/account.html"

    def get(self, request, *args, **kwargs):

        # Checks if user is authentifiacated of has cookies user_id for the authentification
        if request.user.is_authenticated:

            context = {
                "form": None,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email
            }

            return self.render_to_response(context=context)

        elif request.COOKIES.get("*1%", None):

            context = {
                "form": None,
                "user": get_user(request.COOKIES["*1%"]),
                "first_name": get_first_name(request.COOKIES["*1%"]),
                "last_name": get_last_name(request.COOKIES["*1%"]),
                "email": get_email(request.COOKIES["*1%"])
            }

            return self.render_to_response(context=context)

        return self.render_to_response(context={"form": AuthForm(request.GET)})

    def post(self, request, *args, **kwargs):

        # Gets username from form
        username = get_username_by_email(email=request.POST["username"])
        if username is None:
            return redirect("Account")

        # Gets User model instanse to other deeds
        user = authenticate(request, username=username,
                            password=request.POST["password"])

        # Checks whether user is admin to permanent authentification
        if check_admin(username):
            login(request, user)
            return redirect("Account")

        # Checks whether user pressed ratio button and login him
        if request.POST.get("check"):
            if user:
                login(request, user)
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

    template_name = "main/reg.html"
    form_class = RegForm
    success_url = reverse_lazy("Account")

    def form_valid(self,form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)
        return super().get(self.request)



class ServiceList(ListView):
    """Shows us Service List page"""

    template_name = "main/services.html"
    context_object_name = "services"

    def get_queryset(self):
        splited_query = SplitedQuerySet()
        self.queryset = splited_query.get_list(model=Service)
        return self.queryset


class ServiceInfo(DetailView):
    """Shows us page with more detailed info about equal service"""

    template_name = "main/serviceinfo.html"
    context_object_name = "service"
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.COOKIES.get("*1%") or self.request.user.username:
            context["authed"] = True
            context["form"] = RecordForm(self.request.GET)
            return context
        context["authed"] = False
        context["form"] = RecordForm(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        """Saves form data to the db"""

        form = RecordForm(request.POST)
        if form.is_valid():
            if self.request.user.username:
                if form.check(request=self.request):

                    form.save(service_name=request.POST["service_name"])

                    add_message(self.request, SUCCESS,
                                "Вы успешно были записаны")

                    return redirect("ServiceInfo", pk=self.kwargs["pk"])

                add_message(self.request, ERROR,
                            "Вы уже записаны на приём,или произошла ошибка сервера")

                return redirect("ServiceInfo", pk=self.kwargs["pk"])
            elif self.request.COOKIES.get("*1%"):

                if form.check(cookie_request=self.request.COOKIES.get("*1%")):
                    form.save(service_name=request.POST["service_name"])

                    add_message(self.request, SUCCESS,
                                "Вы успешно были записаны")

                    return redirect("ServiceInfo", pk=self.kwargs["pk"])

                add_message(self.request, ERROR,
                            "Вы уже записаны на приём")

                return redirect("ServiceInfo", pk=self.kwargs["pk"])
            else:

                add_message(self.request, ERROR,
                            "Пройзошла ошибка,попробуйте снова")

                return redirect("ServiceInfo", pk=self.kwargs["pk"])

        add_message(self.request, ERROR,
                    "Пройзошла ошибка,попробуйте снова")

        return redirect("ServiceInfo", pk=self.kwargs["pk"])


class ReviewPage(FormView, ListView):

    paginate_by = 4
    model = Review
    template_name = "main/review.html"
    form_class = ReviewForm
    success_url = reverse_lazy("Reviews")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context

    def form_valid(self,form):
        if form.is_valid():
            form.save(request=self.request)
            return super().get(self.request)
        return super().get(self.request)
