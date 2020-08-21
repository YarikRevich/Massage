from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from social.pipeline.user import get_username, create_user
from django.contrib.messages import add_message
from django.contrib.messages import ERROR

        
    