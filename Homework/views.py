from django.shortcuts import render
from django.http import HttpResponse
from emoji import emojize
from .models import Group, User, Deadline
# Create your views here.


def index(request):
    return HttpResponse("First View")


def deadlineDetails(request, deadlineId):
    deadline = Deadline.objects.get(id=deadlineId)
    return HttpResponse(f"You are currently looking at {deadlineId} deadline. \n"
                        f"{deadline}\n"
                        f"Continue watching and you'll get kicked out from university {emojize(':thumbs_up:')}")


def groupDetails(request, groupId):
    group = Group.objects.get(id=groupId)
    users = group.user_set.all()
    userList = ""
    for user in users:
        userList += str(user) + ','
    return HttpResponse(f"this is group {str(group)}. Users = {userList}"
                        f"{emojize(':thinking_face:')}")


def userDetails(request, userId):
    user = User.objects.get(id=userId)
    return HttpResponse(f"this is user {user}. Soon we'll add more info"
                        f"{emojize(':thinking_face:')}")
