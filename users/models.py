from django.contrib.auth.models import AbstractUser
from django.db import models

from service.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')

    number = models.IntegerField(verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватарка', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
