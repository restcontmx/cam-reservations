from rest_framework import serializers
from .models import Task

class TaskSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Task
        fields = ( 'id', 'name', 'description', 'date_end', 'value', 'state', 'user', 'user_assigned', 'timestamp', 'updated', )