from rest_framework import serializers

from ..models import Quiz, Subject, User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    owner = OwnerSerializer()

    class Meta:
        model = Quiz
        fields = ['owner', 'name', 'subject', ]
