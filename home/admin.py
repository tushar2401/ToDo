from django.contrib import admin
from home.models import UserDetails
from home.models import Task

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Task)