from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework import viewsets
from .filters import TaskFilter
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['task_name']
    permission_classes = [permissions.IsAuthenticated]


