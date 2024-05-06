# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from users.Serializer.UserSerializer import (
    CustomUserChangeSerializer,
    CustomUserCreationSerializer,
    LoginSerializer,
)


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]  # 認証されていないユーザーもアクセス可能
    serializer_class = CustomUserCreationSerializer


class UpdateUserView(generics.UpdateAPIView):
    model = get_user_model()
    permission_classes = [permissions.IsAuthenticated]  # 認証が必要
    serializer_class = CustomUserChangeSerializer

    def get_object(self):
        return self.request.user  # 認証されたユーザーのオブジェクトを返す


class LoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
