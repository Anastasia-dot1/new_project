from django.urls import path
from . import views  # Импорт представлений из текущего приложения

urlpatterns = [
    path('', views.caexam_view, name='caexam'),
]