from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from service.models import Subscription
from users.models import User


@shared_task
def check_update_for_courses(title, pk):
    users = User.objects.all()
    users_email = list(user.email for user in users)

    subscriptions = Subscription.objects.filter(course_id=pk)

    users_email_in_subscriptions = list(
        subscription.user.email for subscription in subscriptions if subscription.user.email in users_email
    )

    send_mail(
        subject='Курс обновлён',
        message=f'Курс "{title}" был обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users_email_in_subscriptions

    )
