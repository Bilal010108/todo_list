from rest_framework import  serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task', 'completed','description','created_date' ]










































