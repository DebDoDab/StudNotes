from django.urls import path
from Homework import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deadline/<int:deadlineId>', views.deadlineDetails, name='deadline'),
    path('user/<int:userId>', views.userDetails, name='group'),
    path('group/<int:groupId>', views.groupDetails, name='user'),
]