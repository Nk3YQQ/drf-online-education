from django.contrib.auth.hashers import make_password

from users.models import User


def create_user():
    return User.objects.create(
        first_name='Test',
        last_name='Testov',
        email='test.testov@mail.ru',
        password=make_password('123qwe456rty'),
        is_active=True
    )