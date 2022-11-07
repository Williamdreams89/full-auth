from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework import status

class UserRegisterAPI(GenericAPIView):
    serializer_class = UserRegisterSerializer 

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.validated_data
        user_profile=serializer.save()

        return Response({
            "user_profile": UserRegisterSerializer(user_profile, context = self.get_serializer_context()).data,
            "message": "User Createed successfully",
            "status": status.HTTP_201_CREATED
        })