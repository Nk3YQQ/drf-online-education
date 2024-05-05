import os

from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        moderator_group = Group.objects.get(name='Модератор')

        password = os.getenv('MODERATOR_PASSWORD')

        moderator = User(
            first_name=os.getenv('MODERATOR_NAME'),
            last_name=os.getenv('MODERATOR_SURNAME'),
            email=os.getenv('MODERATOR_EMAIL'),
            is_staff=True
        )

        moderator.set_password(password)
        moderator.save()
        moderator.groups.add(moderator_group)
