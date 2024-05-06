# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from users.Serializer.UserSerializer import (
    CustomUserChangeSerializer,
    CustomUserCreationSerializer,
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
