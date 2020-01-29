from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from emoji import emojize
from .models import Group, User, Deadline
from django.template import loader


# Create your views here.


def index(request):
    return HttpResponse("First View")


def deadlineDetails(request, deadlineId):
    deadline = get_object_or_404(Deadline, id=deadlineId)
    context = {
        'deadlineName': str(deadline),
        'groupName': str(deadline.groupId),
    }
    return render(request, 'deadline.html', context)


def groupDetails(request, groupId):
    group = get_object_or_404(Group, id=groupId)
    userList = ', '.join(str(user) for user in group.user_set.all())
    deadlineList = ', '.join(str(deadline) for deadline in group.deadline_set.all())
    context = {
        'groupName': str(group),
        'userList': userList,
        'deadlineList': deadlineList,
    }
    return render(request, 'group.html', context)


def userDetails(request, userId):
    user = get_object_or_404(User, id=userId)
    context = {
        'userName': str(user),
        'groupName': str(user.groupId),
        'deadlineList': ', '.join(str(deadline) for deadline in Deadline.objects.filter(groupId_id=user.groupId_id)),
    }
    return render(request, 'user.html', context)
