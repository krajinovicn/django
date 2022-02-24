from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import views, viewsets, generics, renderers, permissions
from rest_framework.response import Response
from project.to_do_list.serializers import UserSerializer, ToDoSerializer
from django.contrib.auth.models import User
from project.to_do_list.models import ToDo


def home(request):
    todos = ToDo.objects.all()
    return render(request, "todo_list.html", {"todo_list": todos})


class CurrentUser(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request, format=None):
        self.object = request.user
        return Response({"user": self.object}, template_name="user_details.html")


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({"user": self.object}, template_name="user_details.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
