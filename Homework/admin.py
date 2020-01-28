from django.contrib import admin
from .models import Group, User

# Register your models here.

admin.site.register(Group)
admin.site.register(User)