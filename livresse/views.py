from django.shortcuts import render
from rest_framework import viewsets
from livresse.models import User
from livresse.serializer import UserSerializer

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer