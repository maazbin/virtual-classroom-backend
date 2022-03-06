from django.db import models
# from django.contrib.auth.models import User as owners
from django.db.models.deletion import CASCADE, DO_NOTHING 
import uuid

""" 
    Importing User for the foreign key relationship to associate 
    a specific user (Teacher) with a specific Room.
 """

import uuid
# Create your models here.


# User as students or learner
class User(models.Model):
    id = models.CharField(primary_key=True,unique=True,null=False, max_length=40)
    name = models.CharField(max_length=255, null = True)
    email = models.CharField(max_length=255,null = True)
    

    def __str__(self):
        return self.name

# Room are learning area like courses or classes.
class Room(models.Model):
    # Room_id = models.CharField(primary_key=True, max_length=255)
    Room_name = models.CharField(max_length=255, null = True)
    Room_description = models.CharField(max_length=255, null =True)
    # Enrolled_students = models.ManyToManyField(User, through='Enrollment')

    def __str__(self):
        return self.Room_name


class Enrolment(models.Model):
    class Meta:
        unique_together = ['student', 'room']
    student = models.ForeignKey(User, on_delete=DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=DO_NOTHING)


# Discussion is the place where different Topic are discussed. UI -> Weeks
class Discussion(models.Model):
    discussion_name = models.CharField(max_length=255)
    discussion_description = models.TextField(max_length=255,null = True)
    room = models.ForeignKey(Room, on_delete=DO_NOTHING, default=None, null = False)
    
    def __str__(self):
        return self.discussion_name

# Topic are entities under Discussion where user can post the issue and get the solution.
class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    discussion = models.ForeignKey(Discussion, on_delete=CASCADE, default=None, null=True)
    
    # def __str__(self):
    #     return self.title

# User can answer the question posted in Topic
class Response(models.Model):
    # response_name = models.CharField(max_length=255)
    response_description = models.TextField(max_length=300)
    # response_topic = models.ForeignKey(Topic, on_delete=CASCADE, default=None, null=True)
    # response_user = models.ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    
    # def __str__(self):
    #     return self.response_description

# Comment are under response and have 0 hiraricy and 1 parent (response)
class Comment(models.Model):
    comment_description = models.TextField(max_length=300)
    # comment_response = models.ForeignKey(Response, on_delete=CASCADE, default=None, null=True)
    # comment_user = models.ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    
    # def __str__(self):
    #     return self.comment_description

# class Tasks(models.Model):
#     task_name = models.CharField(max_length=255)
#     task_description = models.TextField(max_length=300)
#     task_Room = models.ForeignKey(Room, on_delete=CASCADE, default=None, null=True)
#     models.ManyToManyField(User)
    
#     def __str__(self):
#         return self.task_name