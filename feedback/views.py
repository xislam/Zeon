from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from feedback.serializers import FeedbackSerializer


class FeedbackCreate(viewsets.ViewSet):
    def create(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
