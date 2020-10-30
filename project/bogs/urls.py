from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blank'),
    path('<str:ide>', views.course, name='course'),
]
