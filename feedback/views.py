from rest_framework.viewsets import ModelViewSet

from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer


class FeedbackCreate(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
