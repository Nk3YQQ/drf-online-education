import os

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from django.db import IntegrityError
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            moderator_group = Group.objects.get(name='Модератор')

            moderator, created = User.objects.get_or_create(
                first_name=os.getenv('MODERATOR_NAME'),
                last_name=os.getenv('MODERATOR_SURNAME'),
                email=os.getenv('MODERATOR_EMAIL'),
                password=make_password(os.getenv('MODERATOR_PASSWORD')),
                is_staff=True
            )

            moderator.groups.add(moderator_group)
            moderator.save()

            if created:
                self.stdout.write(self.style.SUCCESS('Moderator was created'))

        except IntegrityError:
            self.stdout.write('Moderator already exists')
