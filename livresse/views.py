from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from livresse.models import User
from livresse.serializer import UserSerializer

# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer