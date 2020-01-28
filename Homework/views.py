from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from emoji import emojize
from .models import Group, User, Deadline
from django.template import loader


# Create your views here.


def index(request):
    return HttpResponse("First View")


def deadlineDetails(request, deadlineId):
    # TODO template
    deadline = Deadline.objects.get(id=deadlineId)
    return HttpResponse(f"You are currently looking at {deadlineId} deadline. \n"
                        f"{deadline}\n"
                        f"Continue watching and you'll get kicked out from university {emojize(':thumbs_up:')}")


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
    # TODO template
    user = User.objects.get(id=userId)
    return HttpResponse(f"this is user {user}. Soon we'll add more info"
                        f"{emojize(':thinking_face:')}")
