from django.contrib import admin
from django.db import models
# import backend.models as table
from .models import User, Room, Discussion, Topic, Response,Comment
# models_list = [
#     table.User,
#     table.Rooms,
#     table.Discussions,
#     table.Topics,
#     table.Responses,
#     table.Comments
# ]


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Discussion)
admin.site.register(Topic)
admin.site.register(Response)
admin.site.register(Comment)