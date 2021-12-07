from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

		# Model Imports 
from .models import User
from backend import serializers
from .serializers import UserSerializer


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    # return JsonResponse("API BASE POINT",safe=False)
    
    api_urls = {
		'List':'/user-list/',
		# 'Detail View':'/task-detail/<str:pk>/',
		# 'Create':'/task-create/',
		# 'Update':'/task-update/<str:pk>/',
		# 'Delete':'/task-delete/<str:pk>/',
		}


    return Response(api_urls)

# authenticating users from the frontend
@api_view(['GET'])
def userAuth(request,pk,usr,pswrd):
    # return JsonResponse("Task List",safe=False)
    user = User.objects.get(id=pk)
    
    
    if user.username == usr and user.password == pswrd:
        serializer = UserSerializer(user, many=False)
        print(user.username,user.password)
        return Response(serializer.data)
    else:
        return Response({"error":"Invalid Credentials"})


@api_view(['GET'])
def userList(request):
	# return JsonResponse("Task List",safe=False)
	user = User.objects.all()
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)


# Adding Authenticated Users by the firebase to the database

@api_view(['PUT'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)