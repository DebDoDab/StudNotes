from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.


class Group(models.Model):
    groupToken = models.CharField('token for inviting new users from that group', max_length=32)
    name = models.CharField('name of a group (e.g. M3105)', max_length=10)

    def __str__(self):
        return self.name

    def setToken(self):
        token = get_random_string(32)
        while Group.objects.get(groupToken=token):
            token = get_random_string(32)
        self.groupToken = token


class User(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    nickname = models.CharField('just a nickname of a user', max_length=50)
    passHash = models.CharField('hash for matching passwords', max_length=128)

    def __str__(self):
        return self.nickname

    def registration(self, groupToken, nickname, password):
        self.nickname = nickname  # TODO add check on same nicknames
        if User.objects.get(nickname=nickname):
            raise ValueError("Same nick exists")

        self.passHash = password  # TODO add hashing

        group = Group.objects.get(groupToken=groupToken)
        groupId = group.id

    def login(self, nickname, password):
        # TODO log in
        user = User.objects.get(nickname=nickname)
        if not user:
            raise ValueError("No user with such nickname")
        if password == user.passhash:
            return True
        raise ValueError("Wrong Password")


class Deadline(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    expDate = models.DateTimeField('date and time of expiration of a deadline')
    body = models.CharField('some text about this deadline', max_length=228)
    state = models.BooleanField('0 - soft deadline, 1 - hard deadline')

    def __str__(self):
        return self.body

    def addDeadline(self):
        pass
