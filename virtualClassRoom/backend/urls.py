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
    path('topic-list/<int:pk>', views.topicList, name='topic-list'),
    path('user-room-list/<str:pk>', views.userRoomlList, name='user-room-list'),
    path('enrolment', views.enrolment,name='enrolment'),
    path('rooms-of-user/<str:pk>', views.RoomsOfUser, name='rooms-of-user'),
    path('enrol', views.enrol, name='enrol'),
    path('create-topic', views.enrol, name='enrol'), #create a new topic
]
