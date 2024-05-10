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


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'cash', 'Наличные'
        CARD = 'card', 'Перевод на счёт'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='users',
                             **NULLABLE)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey('service.Course', on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE,
                               related_name='courses')
    lesson = models.ForeignKey('service.Lesson', on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE,
                               related_name='lessons')
    amount = models.IntegerField(verbose_name='Сумма оплаты')
    method = models.CharField(max_length=50, choices=PaymentMethod.choices, verbose_name='Способ оплаты')

    session_id = models.CharField(max_length=350, verbose_name='Идентификатор сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)
