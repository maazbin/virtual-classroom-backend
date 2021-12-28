# from backend.views import *


# backend/urls.py
from django.urls import path
from . import views # . means current directory (backend)

urlpatterns = [
    path('api-list', views.apiList, name='api-list'),
    path('user-list', views.userList, name='user-list'),
    path('add-user', views.addUser, name='add-user'),
    path('room-list', views.roomList, name='room-list'),
    path('add-room', views.addRoom, name='add-room'),
    path('disc-list/<int:pk>', views.discList, name='disc-list'),
]
