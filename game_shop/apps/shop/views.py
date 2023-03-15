from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializers import UserProfileSerializer


class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserProfileSerializer