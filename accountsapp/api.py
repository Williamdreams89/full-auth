from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework import status
from .utils import Utils
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegisterAPI(GenericAPIView):
    serializer_class = UserRegisterSerializer 

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.validated_data
        user_profile=serializer.save()

        current_site = get_current_site(request).domain
        rel_url = reverse("verify-email")

        user_data = serializer.data
        user = User.objects.get(email = user_data["email"])
        token = RefreshToken.for_user(user).access_token
        stringified_token= str(token)

        abs_url = "https://{}{}?token={}".format(current_site,rel_url,stringified_token)

        username = user.username
        email_body = "Hi {}, \n Please use click the link below to verify your account: \n {}".format(username, abs_url)
        email_subject = "Account Verification Mail"
        email_to = user.full_name
        data = {"email_subject": email_subject, "email_body":email_body, "email_to":email_to}
        Utils.send_email(data)

        

        return Response({
            "user_profile": UserRegisterSerializer(user_profile, context = self.get_serializer_context()).data,
            "message": "User Createed successfully",
            "status": status.HTTP_201_CREATED
        })


class VerifyEmail(GenericAPIView):
    def get(self):
        pass