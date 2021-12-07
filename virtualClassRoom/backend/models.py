from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    # id = models.UUIDField(primary_key=False,null=True , editable=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # email = models.EmailField()
    # phone = models.CharField(max_length=11)
    # create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Room(models.Model):
        room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        room_name = models.CharField(max_length=20)
        room_password = models.CharField(max_length=20)
        room_create_time = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.room_name