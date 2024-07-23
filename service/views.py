from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from service.models import Course, Lesson, Subscription
from service.paginators import MyPaginator
from service.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from service.tasks import check_update_for_courses
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """ Вьюсет для курсов """

    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('pk')
    pagination_class = MyPaginator

    @swagger_auto_schema(operation_description="Настройка привилегий для курсов")
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]

        return [permission() for permission in permission_classes]

    @swagger_auto_schema(operation_description="Привязка пользователя к курсу")
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @swagger_auto_schema(operation_description="Оповещение пользователя насчёт обновления курса")
    def perform_update(self, serializer):
        course = serializer.save()

        if course:
            check_update_for_courses.delay(course.title, course.pk)

        course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    """ Создание урока """

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    @swagger_auto_schema(operation_description="Привязка пользователя к уроку")
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """ Чтение всех уроков """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all().order_by('course')
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = MyPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Чтение одного урока """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Обновление урока """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Удаление урока """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionAPIView(APIView):
    """ Создание и удаление подписки """

    @swagger_auto_schema(operation_description="Проверка пользователя на подписку")
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course = Course.objects.get(pk=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'подписка активна'

        return Response({'message': message})


class SubscriptionListAPIView(generics.ListAPIView):
    """ Чтение всех подписок """

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
