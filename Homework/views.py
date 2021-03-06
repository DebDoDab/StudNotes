from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from emoji import emojize
from .models import Group, User, Deadline, UnresolvedDeadline
from django.template import loader
from django.urls import reverse


# Create your views here.


def index(request):
    return HttpResponse("First View")


def deadlineDetails(request, deadlineId):
    deadline = get_object_or_404(Deadline, id=deadlineId)
    context = {
        'deadline': deadline,
        'group': deadline.groupId,
        'deadlineExpDate': deadline.expDate.strftime("%Y-%m-%d"),
    }
    return render(request, 'deadline.html', context)


def groupDetails(request, groupId):
    group = get_object_or_404(Group, id=groupId)
    context = {
        'group': group,
        'userList': group.user_set.all(),
        'deadlineList': group.deadline_set.all(),
    }
    return render(request, 'group.html', context)


def userDetails(request, userId):
    user = get_object_or_404(User, id=userId)
    deadlineList = Deadline.objects.filter(groupId_id=user.groupId_id)
    unresolvedDeadlineList = [x.deadlineId for x in UnresolvedDeadline.objects.filter(userId_id=user.id)]
    resolvedDeadlineList = [x for x in deadlineList if x not in unresolvedDeadlineList]
    context = {
        'user': user,
        'group': user.groupId,
        'resolvedDeadlineList': resolvedDeadlineList,
        'unresolvedDeadlineList': unresolvedDeadlineList,
    }
    return render(request, 'user.html', context)


def signuppage(request, registered=False):
    return render(request, 'registration.html', {'registered': registered})


def signupform(request):
    user = User.signup(request.POST['token'], request.POST['nickname'], User.hash(request.POST['password']))
    return HttpResponseRedirect(reverse('homework:user', args=(user.id,)))


def addDeadline(request, groupId):
    group = Group.objects.get(id=groupId)
    deadline = Deadline.objects.create(groupId=group, expDate=request.POST['expdate'], body=request.POST['body'],
                                       state=(1 if 'state' in request.POST else 0))
    deadline.unresolved()

    return HttpResponseRedirect(reverse('homework:group', args=(group.id,)))


def changeDeadlineStatus(request, userId):
    deadlineId = request.POST['deadline']
    if UnresolvedDeadline.objects.filter(deadlineId_id=deadlineId, userId_id=userId):
        ud = UnresolvedDeadline.objects.get(deadlineId_id=deadlineId, userId_id=userId)
        ud.delete()
    else:
        ud = UnresolvedDeadline.objects.create(deadlineId_id=deadlineId, userId_id=userId)

    return HttpResponseRedirect(reverse('homework:user', args=(userId,)))


def deadlineEdit(request, deadlineId):
    deadline = Deadline.objects.get(id=deadlineId)
    deadline.expDate = request.POST['expdate']
    deadline.body = request.POST['body']
    deadline.state = (1 if 'state' in request.POST else 0)
    deadline.save()
    return HttpResponseRedirect(reverse('homework:deadline', args=(deadlineId,)))
