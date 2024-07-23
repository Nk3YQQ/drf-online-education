from rest_framework import status
from rest_framework.test import APITestCase

from service.models import Course, Lesson
from service.services import create_user


class LessonAPITestCase(APITestCase):
    """ Тестирование модели урока """
    def setUp(self) -> None:
        """ Установка данных """

        owner = create_user()

        response = self.client.post(
            '/users/login/', data={"email": "test.testov@mail.ru", "password": "123qwe456rty"}
        )

        self._token = response.json()["access"]

        self.header = {
            "Authorization": f"Bearer {self._token}"
        }

        self.owner = owner

        course = Course.objects.create(
            title='Title',
            description='Description'
        )

        self.lesson_data = {
            "title": "Title",
            "video_url": "https://www.youtube.com/watch?v=ssAiumU",
            "course": course.pk
        }

        self.lesson = {
            "title": "Title",
            "video_url": "https://www.youtube.com/watch?v=ssAiumU",
            "course": course,
            "owner": self.owner
        }

    def test_create_lesson(self):
        """ Тестирование создания урока """

        response = self.client.post(
            '/lessons/create/',
            data=self.lesson_data,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Lesson.objects.all().exists)
        self.assertEqual(response.json()['owner'], self.owner.pk)

    def test_lesson_list(self):
        """ Тестирование списка урока """

        Lesson.objects.create(**self.lesson)

        response = self.client.get(
            '/lessons/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):
        """ Тестирование сущности урока """

        lesson = Lesson.objects.create(**self.lesson)

        response = self.client.get(
            f'/lessons/{lesson.pk}/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """ Тестирование обновления урока """

        lesson = Lesson.objects.create(**self.lesson)

        data = {
            "title": "New lesson"
        }

        response = self.client.patch(
            f'/lessons/edit/{lesson.pk}/',
            data=data,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_delete(self):
        """ Тестирование удаления урока """

        lesson = Lesson.objects.create(**self.lesson)

        response = self.client.delete(
            f'/lessons/delete/{lesson.pk}/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
