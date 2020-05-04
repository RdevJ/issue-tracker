from rest_framework import serializers
from .models import Task, Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer(allow_null=True)

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        status = None
        if 'status' in self.validated_data and self.validated_data['status']:
            status = Status.objects.get(name=self.validated_data['status']['name'])

        instance.status = status if status else instance.status
        instance.title = self.validated_data.get('title', instance.title)
        instance.content = self.validated_data.get('content', instance.content)

        instance.save()
        return instance

class TaskReadSerializer(TaskSerializer):
    status = StatusSerializer(read_only=True)