from django.core.management.base import BaseCommand
from django.utils import timezone

from users.models import User

class Command(BaseCommand):
    help = 'Seed users into the database'

    def handle(self, *args, **options):
        users = [
            {
                'name': 'User one',
                'email': 'user.one@example.com',
                'password': 'Password@123',
                'access_token': None,
                'is_admin': False,
                'created_at': timezone.now()
            },
            {
                'name': 'User two',
                'email': 'user.two@example.com',
                'password': 'Password@123',
                'access_token': None,
                'is_admin': False,
                'created_at': timezone.now()
            },
            {
                'name': 'User three',
                'email': 'user.three@example.com',
                'password': 'Password@123',
                'access_token': None,
                'is_admin': False,
                'created_at': timezone.now()
            },
            {
                'name': 'Admin one',
                'email': 'admin.one@example.com',
                'password': 'Password@123',
                'access_token': None,
                'is_admin': True,
                'created_at': timezone.now()
            },
            {
                'name': 'Admin two',
                'email': 'admin.two@example.com',
                'password': 'Password@123',
                'access_token': None,
                'is_admin': True,
                'created_at': timezone.now()
            }
        ]

        for user_data in users:
            User.objects.get_or_create(
                email=user_data['email'],
                defaults={
                    'name': user_data.get('name'),
                    'password': user_data['password'],
                    'is_admin': user_data.get('is_admin', False),
                    'created_at': timezone.now(),
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully seeded user: {user_data["email"]}'))
