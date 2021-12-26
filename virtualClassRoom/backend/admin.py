from django.contrib import admin
from django.db import models
import backend.models as tables

models_list = {
    'User': tables.User,
    # tables.Rooms,
    # tables.Discussions,
    # tables.Topics,
    # tables.Responses,
    # tables.Comments
}


admin.site.register(models_list['User'])
# admin.site.register(tables.Rooms)
# admin.site.register(tables.Discussions)
# admin.site.register(tables.Topics)
# admin.site.register(tables.Responses)
# admin.site.register(tables.Comments)