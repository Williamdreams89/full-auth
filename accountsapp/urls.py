from django.urls import path
from .api import UserRegisterAPI, VerifyEmail

urlpatterns = [
    path("user/signup/", UserRegisterAPI.as_view(), name="user-signup" ),
    path("user/signup/verify-email/", VerifyEmail.as_view(), name="verify-email" ),
]