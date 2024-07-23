from django.core.management import BaseCommand

from payment.models import Payment
from service.models import Course, Lesson
from users.models import User
from payment.services import convert_payment_to_data


class Command(BaseCommand):
    """ Наполнение данными из фикстур """

    def handle(self, *args, **options):
        payment_data = convert_payment_to_data()

        payments = []
        for data in payment_data:
            user_id = data.pop('user')
            user = User.objects.get(pk=user_id)

            course = None
            lesson = None

            if data.get('course') is not None:
                payment_id = data.pop('course')
                course = Course.objects.get(pk=payment_id)
            elif data.get('lesson') is not None:
                lesson_id = data.pop('lesson')
                lesson = Lesson.objects.get(pk=lesson_id)

            payment = Payment(user=user, **data)

            payment.course = course
            payment.lesson = lesson

            payments.append(payment)

        Payment.objects.bulk_create(payments)
