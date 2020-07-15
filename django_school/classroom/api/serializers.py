from rest_framework import serializers

from ..models import Quiz, Subject, User, Question


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    owner = OwnerSerializer()
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['owner', 'name', 'subject', 'questions']
