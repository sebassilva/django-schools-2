from rest_framework import viewsets

from .serializers import QuizSerializer
from ..models import Quiz


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        return self.queryset
