from django.urls import path
from Homework import views


app_name = 'homework'
urlpatterns = [
    path('', views.index, name='index'),
    path('deadline/<int:deadlineId>', views.deadlineDetails, name='deadline'),
    path('user/<int:userId>', views.userDetails, name='user'),
    path('group/<int:groupId>', views.groupDetails, name='group'),
    path('signup/', views.signuppage, name='signuppage'),
    path('signup/submit', views.signupform, name='signupform'),
]