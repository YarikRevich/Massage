from django.apps import AppConfig
from social_django.config import PythonSocialAuthConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Основное'


class SocialConfig(PythonSocialAuthConfig):
    verbose_name = "Аутентификация через соц.сети"
