from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blank'),    
    path('persons/', views.PersonList.as_view(), name='list'),
    path('persons/<str:pk>/', views.PersonDetail.as_view(),name='personinfo'),
    path('<str:ide>', views.course, name='course'),
]
