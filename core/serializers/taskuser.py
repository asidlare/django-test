from rest_framework import serializers

from core.models import TaskUser


class TaskUserSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='id', read_only=True)
    userEmail = serializers.EmailField(source='email')
    userFirstName = serializers.CharField(source='first_name', default='')
    userLastName = serializers.CharField(source='last_name', default='')
    userDateOfBirth = serializers.DateField(source='date_of_birth', default=None)
    userCreatedAt = serializers.DateTimeField(source='created_at', read_only=True)
    userUpdatedAt = serializers.DateTimeField(source='updated_at', read_only=True)

    class Meta:
        model = TaskUser
        fields = (
            'userId',
            'userEmail',
            'userFirstName',
            'userLastName',
            'userDateOfBirth',
            'userCreatedAt',
            'userUpdatedAt',
        )
        read_only_fields = ('userId', 'userCreatedAt', 'userUpdatedAt')
