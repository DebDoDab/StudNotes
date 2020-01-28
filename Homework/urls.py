from django.urls import path
from Homework import views

urlpatterns = [
    path('', views.index, name='index')
]