from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import TaskUser
from core.serializers.taskuser import TaskUserSerializer


class TaskUserAPIView(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, id=None):
        if id:
            user = get_object_or_404(TaskUser, id=id)
            serializer = TaskUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        users = TaskUser.objects.all()
        serializer = TaskUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer = TaskUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if any([field for field in request.data if field in ('userId','createdAt', 'updatedAt')]):
            return Response(
                {'detail': 'userId, createdAt, updatedAt cannot be changed manually.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = get_object_or_404(TaskUser, id=id)
        serializer = TaskUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        user = get_object_or_404(TaskUser, id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
