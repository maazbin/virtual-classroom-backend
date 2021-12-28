from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

		# Model Imports 
from .models import User,Room,Discussion

        # serializers Imports
from backend import serializers
from .serializers import UserSerializer,RoomSerializer,DiscussionSerializer




# Listing available APIs
@api_view(['GET'])
def apiList(request):
    # return JsonResponse("API BASE POINT",safe=False)
    
    api_urls = {
		'API List':'api/user-list/',
		'Add a new user':'api/add-user',
		'User list':'api/user-list/',
        'Room list':'api/room-list/',
        'Add a new room':'api/add-room',
        'Get Discussion list':'api/disc-list/<str:pk>',
		# 'Update':'/task-update/<str:pk>/',
		# 'Delete':'/task-delete/<str:pk>/',
		}


    return Response(api_urls)

# Adding Authenticated Users by the firebase to the database
@api_view(['GET'])
def userList(request):
	# return JsonResponse("Task List",safe=False)
	user = User.objects.all()
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)




@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addRoom(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#loading the room list
@api_view(['GET'])
def roomList(request):
    # return JsonResponse("Task List",safe=False)
    room = Room.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


#List of discussions -> week in UI
@api_view(['GET'])
def discList(request,pk):
    discussion = Discussion
    room = Room.objects.get(pk=pk)
    # for disc in Discussion.objects.filter(discussion_Room=room):
    #     print(disc.discussion_name)
    discussion = Discussion.objects.filter(discussion_Room=room)
    if discussion.count() == 0:
        return Response("No Discussions")
   
    serializer = DiscussionSerializer(discussion, many=True)

    return Response(serializer.data)
   
