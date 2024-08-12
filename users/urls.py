from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from . import views

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token-refresh'),

    path('create/', views.UserCreateAPIView.as_view(), name='create'),
    path('list/', views.UserListAPIView.as_view(), name='list'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>/', views.UserRetrieveAPIView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.UserDestroyAPIView.as_view(), name='delete')
]
