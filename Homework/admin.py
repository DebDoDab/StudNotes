from django.contrib import admin
from .models import Group, User, Deadline, UnresolvedDeadline

# Register your models here.

admin.site.register(Group)
admin.site.register(User)
admin.site.register(Deadline)
admin.site.register(UnresolvedDeadline)
