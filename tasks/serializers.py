# tasks/serializers.py
from rest_framework import serializers
from tasks import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'title',
            'description',
            'dueDate',
            'priority',
            'isComplete',
            'taskImage',
            'createdAt',
            'updatedAt'
        )
        model = models.Task
