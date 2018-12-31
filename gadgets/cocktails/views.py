from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from gadgets.cocktails.serializers import UserSerializer, GroupSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the cocktails index.")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
