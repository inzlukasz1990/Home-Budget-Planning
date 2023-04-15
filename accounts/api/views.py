from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import RegisterUserSerializer

User = get_user_model()

# ---API---

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

class LoginUserView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
