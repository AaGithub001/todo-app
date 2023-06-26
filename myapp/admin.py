from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserModel)
admin.site.register(TodoModel)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(TagModel)
