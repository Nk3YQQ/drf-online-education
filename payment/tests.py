from rest_framework import status
from rest_framework.test import APITestCase

from payment.models import Payment
from service.models import Course
from service.utils import create_user


class PaymentAPITestCase(APITestCase):
    """ Тестирование оплаты """

    def setUp(self):
        """ Установка данных """

        self.user = create_user()

        response = self.client.post("/users/login/", data={"email": "test.testov@mail.ru", "password": "123qwe456rty"})

        self.token = response.json()['access']

        self.header = {"Authorization": f"Bearer {self.token}"}

        course = Course.objects.create(
            title='Title',
            description='Description'
        )

        self.payment_data = {
            "course": course.pk,
            "amount": 1000,
            "method": "card"
        }

        self.payment = {
            "course": course,
            "amount": 1000,
            "method": "card",
            "user": self.user
        }

    def test_create_payment(self):
        """ Тестирование создания оплаты """

        response = self.client.post('/payment/create/', data=self.payment_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_payment_list(self):
        """ Тестирование списка оплат """

        Payment.objects.create(**self.payment)

        response = self.client.get('/payment/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_payment_retrieve(self):
        """ Тестирование одной оплаты """

        payment = Payment.objects.create(**self.payment)

        response = self.client.get(f'/payment/{payment.pk}/', headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
