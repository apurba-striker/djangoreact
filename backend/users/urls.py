from django.urls import path
from .views import RegisterView,LoginView,UserProfileView, UserUpdateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'auth_register'),
    path('login/',LoginView.as_view(), name = 'auth_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'tokens_refresh'),
    path('profile/', UserProfileView.as_view(), name = 'user_profile'),
    path('profile/update/', UserUpdateView.as_view(), name = 'user_update'),
]
