from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from users.models import User


@shared_task
def check_user_for_active():
    """ Функция блокирует пользователя, если он не заходил более 1 месяца """
    now = timezone.now()
    one_month_ago = now - timedelta(days=30)

    users = User.objects.all()

    for user in users:
        if user.last_login > one_month_ago:
            send_mail(
                subject='Ваш аккаунт заблокирован',
                message=f"""{user}, ваш аккаунт был заблокирован, так как вы не заходили более 1 месяца. 
                Пожалуйста, восстановите его в личном кабинете как можно скорее!""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            user.is_active = False
