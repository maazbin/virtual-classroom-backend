from django.db import models
# import uuid
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=140, default='SOME STRING')
    email = models.CharField(max_length=140, default='SOME STRING')
    # # # # phone = models.CharField(max_length=11)
    # # # create_time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name




# class Room(models.Model):
#     # room_id = models.CharField(primary_key=True, max_length=255)
#     room_name = models.CharField(max_length=255)
#     user = models.ManyToManyField(User)
