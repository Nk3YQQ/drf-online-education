from rest_framework import status
from rest_framework.test import APITestCase

from service.services import create_user, create_other_user


class UserAPITestCase(APITestCase):
    """ Тестирование пользователей """

    def setUp(self):
        """ Установка данных """

        self.user = create_user()
        self.other_user = create_other_user()

        response = self.client.post("/users/login/", data={"email": "test.testov@mail.ru", "password": "123qwe456rty"})

        response_for_other_owner = self.client.post(
            "/users/login/", data={"email": "ivan.ivanov@mail.ru", "password": "123qwe456rty"}
        )

        self.token = response.json()['access']
        self.other_owner_token = response_for_other_owner.json()['access']

        self.header = {"Authorization": f"Bearer {self.token}"}
        self.other_owner_header = {"Authorization": f"Bearer {self.other_owner_token}"}

        self.patch_data = {"first_name": "Test1"}

    def test_user_retrieve(self):
        """ Тестирование просмотра пользователя """

        response = self.client.get(f"/users/{self.user.pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_retrieve_for_other_user(self):
        """Тестирование просмотра пользователя для другого пользователя"""

        response = self.client.get(f"/users/{self.user.pk}/", headers=self.other_owner_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        """ Тестирование обновления пользователя """

        response = self.client.patch(f"/users/edit/{self.user.pk}/", data=self.patch_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_for_other_user(self):
        """Тестирование обновления пользователя для другого пользователя"""

        response = self.client.patch(
            f"/users/edit/{self.user.pk}/", data=self.patch_data, headers=self.other_owner_header
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_destroy(self):
        """Тестирование удаление пользователя"""

        response = self.client.delete(f"/users/delete/{self.user.pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_destroy_for_other_user(self):
        """Тестирование удаление пользователя для другого пользователя"""

        response = self.client.delete(f"/users/delete/{self.user.pk}/", headers=self.other_owner_header)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
