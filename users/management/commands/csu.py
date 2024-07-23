import os

from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from django.db import IntegrityError
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            superuser, created = User.objects.get_or_create(
                first_name=os.getenv('ADMIN_NAME'),
                last_name=os.getenv('ADMIN_SURNAME'),
                email=os.getenv('ADMIN_EMAIL'),
                password=make_password(os.getenv('ADMIN_PASSWORD')),
                is_staff=True,
                is_superuser=True
            )

            if created:
                self.stdout.write(self.style.SUCCESS('User "Admin" was created'))

        except IntegrityError:
            self.stdout.write('User "Admin" already exists')
