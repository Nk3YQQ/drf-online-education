from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from service.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        permission_classes = [IsAuthenticated]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated]

    @staticmethod
    def get_lesson_count(instance):
        return instance.lessons.count()
