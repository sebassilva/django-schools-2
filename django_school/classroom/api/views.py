from rest_framework import filters
from rest_framework import viewsets

from .serializers import QuizSerializer
from ..models import Quiz


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['questions__text']

    def get_queryset(self):
        return self.queryset
