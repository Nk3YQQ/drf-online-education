from django.urls import path

from service.apps import ServiceConfig
from rest_framework.routers import DefaultRouter

from service.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

app_name = ServiceConfig.name

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/edit/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_edit'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete')
] + router.urls
