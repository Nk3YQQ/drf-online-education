from rest_framework import status
from rest_framework.test import APITestCase

from service.models import Course
from service.services import create_user


class SubscriptionAPITestCase(APITestCase):
    """ Тестирование модели подписки """
    def setUp(self) -> None:
        """ Установка данных """

        self.owner = create_user()

        response = self.client.post(
            '/users/login/', data={"email": "test.testov@mail.ru", "password": "123qwe456rty"}
        )

        self._token = response.json()["access"]

        self.header = {
            "Authorization": f"Bearer {self._token}"
        }

        course = Course.objects.create(
            title='Title',
            description='Description'
        )

        self.subscription = {
            "course_id": course.pk,
        }

    def test_activate_and_deactivate_subscription(self):
        """ Тестирование создания подписки """

        response = self.client.post(
            '/subscriptions/activate/',
            data=self.subscription,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['message'],
            'подписка активна'
        )

        response = self.client.post(
            '/subscriptions/activate/',
            data=self.subscription,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['message'],
            'подписка удалена'
        )
