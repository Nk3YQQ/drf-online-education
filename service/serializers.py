from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import UniqueTogetherValidator

from service.models import Course, Lesson, Subscription
from service.validators import CheckLessonURLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        permission_classes = [IsAuthenticated]
        validators = [
            CheckLessonURLValidator(field='video_url'),
            UniqueTogetherValidator(
                fields=('title',),
                queryset=Lesson.objects.all(),
                message='Заголовок должен быть уникальным для каждого урока'
            )
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = '__all__'
        permission_classes = [IsAuthenticated]
        validators = [
            UniqueTogetherValidator(
                fields=('title',),
                queryset=Course.objects.all(),
                message='Заголовок должен быть уникальным для каждого курса'
            )
        ]

    @staticmethod
    def get_lesson_count(instance):
        return instance.lessons.count()

    def get_subscription(self, instance):
        user = self.context['request'].user
        return 'Активирована' if Subscription.objects.filter(user=user, course=instance).exists() else 'Не активирована'
