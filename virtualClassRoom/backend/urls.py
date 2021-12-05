# from backend.views import *


# backend/urls.py
from django.urls import path
from . import views # . means current directory (backend)

urlpatterns = [
    path('user-auth/<str:pk>&&<str:usr>&&<str:pswrd>', views.userAuth, name='user-auth'),
    path('user-list', views.userList, name='user-list'),
]
