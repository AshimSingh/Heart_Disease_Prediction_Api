from rest_framework import serializers

from prediction.models import Question,Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']

class QuestionSerializer(serializers.ModelSerializer):
       choices = ChoiceSerializer(many=True, read_only=True)
       class Meta:
        model = Question
        fields = ['id', 'question', 'choices', 'votes']
        

