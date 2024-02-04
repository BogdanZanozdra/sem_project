from django.core.management.base import BaseCommand

from app_1.models import Author


class Command(BaseCommand):
    help = 'delete an author by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Author id to delete')

    def handle(self, *args, **kwargs):
        id = kwargs['id']

        author = Author.objects.filter(pk=id).first()

        author.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author: {author}'))
