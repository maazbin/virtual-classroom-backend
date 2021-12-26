from django.db import models
# from django.contrib.auth.models import User as owners
from django.db.models.deletion import CASCADE, DO_NOTHING 
import uuid

""" 
    Importing User for the foreign key relationship to associate 
    a specific user (Teacher) with a specific room.
 """

# import uuid
# Create your models here.


# User as students or learner
class User(models.Model):
    # id = models.CharField(max_length=100,primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=140, default='SOME STRING')
    email = models.CharField(max_length=140, default='SOME STRING')
    # # # # phone = models.CharField(max_length=11)
    # # # create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Rooms are learning area like courses or classes.
class Rooms(models.Model):
    # room_id = models.CharField(primary_key=True, max_length=255)
    # owner = models.ForeignKey(owners, db_column="user",on_delete=DO_NOTHING,default=None,null=True)
    room_name = models.CharField(max_length=255)
    # room_description = models.CharField(max_length=2551)
    Enrolled_students = models.ManyToManyField(User)

    def __str__(self):
        return self.room_name

# Discussion is the place where different topics are discussed. UI -> Week
class Discussions(models.Model):
    discussion_name = models.CharField(max_length=255)
    discussion_description = models.TextField(max_length=255)
    discussion_room = models.ForeignKey(Rooms, on_delete=CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.discussion_name

# Topics are entities under Discussions where user can post the issue and get the solution.
class Topics(models.Model):
    topic_name = models.CharField(max_length=255)
    topic_description = models.TextField(max_length=255)
    topic_discussion = models.ForeignKey(Discussions, on_delete=CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.topic_name

# User can answer the question posted in Topics
class Responses(models.Model):
    # response_name = models.CharField(max_length=255)
    response_description = models.TextField(max_length=300)
    response_topic = models.ForeignKey(Topics, on_delete=CASCADE, default=None, null=True)
    response_user = models.ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    
    # def __str__(self):
    #     return self.response_description

# Comments are under response and have 0 hiraricy and 1 parent (response)
class Comments(models.Model):
    comment_description = models.TextField(max_length=300)
    comment_response = models.ForeignKey(Responses, on_delete=CASCADE, default=None, null=True)
    comment_user = models.ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    
    # def __str__(self):
    #     return self.comment_description

# class Tasks(models.Model):
#     task_name = models.CharField(max_length=255)
#     task_description = models.TextField(max_length=300)
#     task_room = models.ForeignKey(Rooms, on_delete=CASCADE, default=None, null=True)
#     models.ManyToManyField(User)
    
#     def __str__(self):
#         return self.task_name