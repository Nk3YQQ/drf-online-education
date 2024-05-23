from django.urls import path

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView,
                         UserDestroyAPIView)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    # User
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('edit/<int:pk>/', UserUpdateAPIView.as_view(), name='user_edit'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
