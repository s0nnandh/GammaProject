from django.urls import path
from django.contrib.auth import login
from . import views

urlpatterns = [
    path('', views.home, name='blank'),    
    path('persons/', views.PersonList.as_view(), name='list'),
    path('persons/<str:pk>/', views.PersonDetail.as_view(),name='personinfo'),
    path('<str:ide>', views.course, name='course'),
    path('<str:ide>/manage', views.manage, name='manage students'),
]
