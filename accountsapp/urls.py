from django.urls import path
from .api import UserRegisterAPI

urlpatterns = [
    path("user/signup/", UserRegisterAPI.as_view(), name="user-signup" ),
]