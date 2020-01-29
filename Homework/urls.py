from django.urls import path
from Homework import views


app_name = 'homework'
urlpatterns = [
    path('', views.index, name='index'),
    path('deadline/<int:deadlineId>/', views.deadlineDetails, name='deadline'),
    path('deadline/<int:deadlineId>/edit_deadline', views.deadlineEdit, name='deadlineedit'),
    path('user/<int:userId>/', views.userDetails, name='user'),
    path('user/<int:userId>/change_deadline_status/', views.changeDeadlineStatus, name='changedeadlinestatus'),
    path('group/<int:groupId>/', views.groupDetails, name='group'),
    path('group/<int:groupId>/add_deadline/', views.addDeadline, name='adddeadline'),
    path('signup/', views.signuppage, name='signuppage'),
    path('signup/submit/', views.signupform, name='signupform'),
]