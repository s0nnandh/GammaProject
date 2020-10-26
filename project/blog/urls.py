from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
]