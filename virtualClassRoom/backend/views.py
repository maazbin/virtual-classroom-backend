from unicodedata import name
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

		# Model Imports 
from .models import Topic, User,Room,Discussion,Enrolment
from .models import Responses

        # serializers Imports
from backend import serializers
from .serializers import UserSerializer,RoomSerializer,DiscussionSerializer,EnrolmentSerializer,TopicSerializer,ResponsesSerializer,CommentSerializer




# Listing available APIs
@api_view(['GET'])
def apiList(request):
    # return JsonResponse("API BASE POINT",safe=False)
    
    api_urls = {
		'Get API List':'api/user-list/',
        'Get Comments of a Response with users (pass response id)':'api/comment-list/<int:pk>', #pass response id
        'Get Responses of a topic with users (pass topic id)':'api/response-list/<int:pk>', #pass topic id
		'Get Discussion list of a room':'api/disc-list/<int:pk>',# pk = room id
        'Get Topics list of a Discussion':'api/topic-list/<int:pk>',
        'Get Users in the req room' : 'api/user-room-list/<str:pk>', #pass room id
        'Get room(s) for an enrolled specific user': 'api/rooms-of-user/<str:pk>', # pass user id
		'Get User list':'api/user-list/',
        'Get Room list':'api/room-list/',
        'Add a new user':'api/add-user',
        'Add a new room':'api/add-room',
        'Enrolling a user in a group' : 'api/enrolment', # post user and room id
        'Create a new topic':'api/create-topic', #accepts title , description, discussion id
        'Creates a new response for a topic(accepts response_description,response_user , response_topic)' : 'api/create-response', #accepts response text,user id , topic id
        'Creates a new response for a topic(accepts comment_description,comment_response ,comment_user)' : 'api/create-comment', #accepts comment text,user id , response id
		}


    return Response(api_urls)

# Adding Authenticated Users by the firebase to the database
@api_view(['GET'])
def userList(request):
	# return JsonResponse("Task List",safe=False)
	user = User.objects.all()
	serializer = UserSerializer(user, many=True)
	return Response(serializer.data)


# add new user 

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# add new room

@api_view(['POST'])
def addRoom(request):
    serializer = RoomSerializer(data=request.data)
    disc = Discussion
    #to get max from room id
    from django.db.models import Max
    if serializer.is_valid():
        serializer.save()
        # adding 3 weeks in the new room
        r = Room.objects.all().aggregate(Max('id'))
        r = Room.objects.get(id=r['id__max'])
        for x in range(3):
            disc = Discussion(discussion_name = f'Week {x}', discussion_description = f'this is week {x}', room = r) 
            disc.save()
        # print()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#loading the room list
@api_view(['GET'])
def roomList(request):
    # return JsonResponse("Task List",safe=False)
    room = Room.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


#List of discussions -> week in UI in a Room
@api_view(['GET'])
def discList(request,pk): #pk is the room id
    discussion = Discussion
    rooms = Room.objects.get(pk=pk)

    discussion = Discussion.objects.filter(room=rooms)
    if discussion.count() == 0:
        return Response([])
   
    serializer = DiscussionSerializer(discussion, many=True)

    return Response(serializer.data)

#List of Topic -> Topic in a Discussion
@api_view(['GET'])
def topicList(request,pk): #pk is the Discussion id
    topic = Topic
    disc = Discussion.objects.get(pk=pk)

    topic = Topic.objects.filter(discussion=disc)
    if topic.count() == 0:
        return Response([])
   
    serializer = TopicSerializer(topic, many=True)
    return Response(serializer.data)    
   

# Enrolled users
@api_view(['GET'])
def userRoomlList(request,pk):
    enrol = Enrolment
    
    #getting data of room for a spesific user 
    enrol = Enrolment.objects.filter(room = pk)
    
    if enrol.count() == 0:
        return Response([])
   
    serializer = EnrolmentSerializer(enrol, many=True)
    return Response(serializer.data)


# Enrol a user in a room
@api_view(['POST'])
def enrolment(request):
    serializer = EnrolmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create a new Topic in 
@api_view(['POST'])
def createTopic(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """
        For more work on the query regarding studetns enrolled in a room

        CODE;

     for x in user.objects.all():
         enrol = Enrolment(room =Room.objects.get(id = 27) , student = user.objects.get(id = x.id))
         enrol.save()        
    """

    
# Returning a room(s) for a specifics user
@api_view(['GET'])
def RoomsOfUser(request,pk):
#    if request.method == 'GET':
    enrol = Enrolment
    
    #getting data of room for a spesific user 
    enrol = Enrolment.objects.filter(student = pk)
    
    if enrol.count() == 0:
        return Response([])
    roomList = {}
    for e in Enrolment.objects.filter(student = pk):
        roomList[e.room.Room_name] = e.room.id
    # resList = [roomList,enrol.count()]
    return JsonResponse(roomList)



# Get pairs of all users and rooms (enrolled)
@api_view(['GET'])
def enrol(request):
    enrol = Enrolment
    enrol = Enrolment.objects.all()
    serializer = EnrolmentSerializer(enrol,many = True)
    return Response(serializer.data) 


# Create a new response for the topic
@api_view(['POST'])
def createResponse(request):
    serializer = ResponsesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Get responses of a topic by the users 
@api_view(['GET'])
def responseList(request,pk): #pk is the topic id
    
    topic = Topic.objects.get(pk=pk)
    resp = Responses.objects.filter(response_topic=topic)
    if resp.count == 0 :
        return([])        
    serializer = ResponsesSerializer(resp, many=True)
    return Response(serializer.data)
    

#Creates a new comment for a response
@api_view(['POST'])
def createComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get comments of a response by the user 
@api_view(['GET'])
def commentList(request,pk): #pk is the topic id
    
    resp = Responses.objects.get(pk=pk)
    comment = Comment.objects.filter(comment_response=resp)
    if comment.count == 0 :
        return([])        
    serializer = ResponsesSerializer(resp, many=True)
    return Response(serializer.data)