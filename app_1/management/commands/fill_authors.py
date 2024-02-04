import datetime

from django.core.management.base import BaseCommand
from app_1.models import  Author

class Command(BaseCommand):
    help = 'Create new users'

    def handle(self, *args, **options) -> str | None:
        for i in range(1, 11):
            author = Author(
                name=f'Author {i}',
                last_name=f'Last Name: {i}',
                email=f'{i}@mail.com',
                bio='Lorem ipsum',
                birthday=datetime.date(2000, 1, 1)
            )
            self.stdout.write(self.style.ERROR(f'Author {author} created.'))
            author.save()
