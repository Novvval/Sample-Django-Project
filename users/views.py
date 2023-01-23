from django.contrib.auth import login
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import CreateUserSerializer, LoginSerializer


class RegisterView(CreateAPIView):
    """Вью для регистрации пользователя"""
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class LoginView(CreateAPIView):
    """Вью для логина пользователя"""
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())