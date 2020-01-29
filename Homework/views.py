from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from emoji import emojize
from .models import Group, User, Deadline
from django.template import loader
from django.urls import reverse


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


def signuppage(request, registered=False):
    return render(request, 'registration.html', {'registered': registered})


def signupform(request):
    token = request.POST['token']
    nickname = request.POST['nickname']
    password = request.POST['password']
    group = get_object_or_404(Group, groupToken=token)
    if User.objects.filter(nickname=nickname):
        raise ValueError("User with such nickname already exists")
    group.user_set.create(nickname=nickname, passHash=password)
    user = User.objects.get(nickname=nickname)

    return HttpResponseRedirect(reverse('homework:user', args=(user.id,)))
