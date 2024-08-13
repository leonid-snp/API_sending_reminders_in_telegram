from django.urls import path

from habit.apps import HabitConfig

from . import views

app_name = HabitConfig.name

urlpatterns = [
    path('create/', views.HabitCreateAPIView.as_view(), name='create'),
    path('list/', views.HabitListAPIView.as_view(), name='list'),
    path('update/<int:pk>/', views.HabitUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>/', views.HabitRetrieveAPIView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.HabitDestroyAPIView.as_view(), name='delete')
]
