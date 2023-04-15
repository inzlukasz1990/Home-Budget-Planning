from django.urls import path
from .views import RegisterUserView, LoginUserView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
