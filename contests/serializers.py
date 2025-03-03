from rest_framework import serializers
from .models import Contest, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'contest_id', 'index', 'name', 'rating', 'tags']  # ✅ ID include kiya

class ContestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)  # ✅ Read-Only Questions Data
    question_ids = serializers.ListField(write_only=True, child=serializers.IntegerField(), required=True)  # ✅ Required Selected Questions

    class Meta:
        model = Contest
        fields = ['id', 'name', 'start_time', 'end_time', 'created_by', 'questions', 'question_ids']

    def create(self, validated_data):
        question_ids = validated_data.pop('question_ids', [])
        contest = Contest.objects.create(**validated_data)
        contest.questions.set(Question.objects.filter(id__in=question_ids))  # ✅ Selected Questions Add Karna
        return contest
