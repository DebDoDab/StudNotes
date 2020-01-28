from django.db import models

# Create your models here.


class Group(models.Model):
    groupId = models.IntegerField()
    groupToken = models.IntegerField()
    name = models.CharField(max_length=10)


class User(models.Model):
    userId = models.IntegerField()
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    passHash = models.CharField(max_length=128)
