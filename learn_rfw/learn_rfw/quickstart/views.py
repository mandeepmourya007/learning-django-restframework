from django.shortcuts import render

from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from learn_rfw.quickstart.serializers import UserSerializer,GroupSerializer

'''  NOTE  queryset and serilizer_class is required '''
#view for User serializer
class UserViewSet(viewsets.ModelViewSet):

    #API to see all users
    queryset = User.objects.all()
    
    #  we need to tell which serializer to be used
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    #to see all groups
    queryset = Group.objects.all()

    #serializer to be used
    serializer_class = GroupSerializer
