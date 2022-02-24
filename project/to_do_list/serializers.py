from django.contrib.auth.models import User
from project.to_do_list.models import ToDo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name",
                  "username", "email", "password"]


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
