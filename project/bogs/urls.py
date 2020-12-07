from django.urls import path
from django.contrib.auth import login
from . import views

urlpatterns = [
    path('', views.home, name='blank'),
    path('messages/<str:pk>/',views.MessageDetail.as_view(),name='messageinfo'),
    path('groups/',views.GroupList.as_view(),name='group_list'),
    path('groups/<str:pk>/',views.GroupDetail.as_view(),name = 'groupinfo'),    
    path('persons/', views.PersonList.as_view(), name='list'),
    path('persons/<str:pk>/', views.PersonDetail.as_view(),name='personinfo'),
    path('<str:ide>', views.course, name='course'),
    path('<str:ide>/manage', views.manage, name='manage students'),
    path('<str:ide>/manage/TA', views.ta, name='manage students'),
]
