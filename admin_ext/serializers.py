from rest_framework import serializers
from .models import Task

class TaskSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Task
        fields = ( 'name', 'description', 'date_end', 'user', 'user_assigned', 'timestamp', 'updated', )