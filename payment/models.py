from django.db import models

from service.models import NULLABLE


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'cash', 'Наличные'
        CARD = 'card', 'Перевод на счёт'

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', related_name='users',
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
