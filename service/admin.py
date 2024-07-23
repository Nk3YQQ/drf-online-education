from django.contrib import admin

from service.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """ Админка для курса """

    list_display = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """ Админка для урока """

    list_display = ('title',)
