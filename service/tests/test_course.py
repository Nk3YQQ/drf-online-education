from rest_framework import status
from rest_framework.test import APITestCase

from service.models import Course
from service.utils import create_user


class CourseAPITestCase(APITestCase):
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

        self.course_data = {
            "title": "Title",
            "description": "Description",
        }

        self.course = {
            "title": "Title",
            "description": "Description",
            "owner": self.owner
        }

    def test_course_create(self):
        """ Тестирование создания курса """

        response = self.client.post(
            '/courses/',
            data=self.course_data,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Course.objects.all().exists)
        self.assertEqual(response.json()['owner'], self.owner.pk)

    def test_lesson_list(self):
        """ Тестирование списка курса """

        Course.objects.create(**self.course)

        response = self.client.get(
            '/courses/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_retrieve(self):
        """ Тестирование сущности курса """

        course = Course.objects.create(**self.course)

        response = self.client.get(
            f'/courses/{course.pk}/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_update(self):
        """ Тестирование обновления курса """

        course = Course.objects.create(**self.course)

        data = {
            "title": "New course"
        }

        response = self.client.patch(
            f'/courses/{course.pk}/',
            data=data,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_delete(self):
        """ Тестирование удаления курса """

        course = Course.objects.create(**self.course)

        response = self.client.delete(
            f'/courses/{course.pk}/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
