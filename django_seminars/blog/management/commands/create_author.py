from django.core.management.base import BaseCommand
from ...models import Author
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = 'create authors'

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(
                first_name = f'First_name_{i}',
                last_name = f'Last_name_{i}',
                email = f'Name_{i}@mail.ru',
                bio = '. '.join(lorem_ipsum.paragraphs(5, common=False)),
                birth_date = '2000-01-12'
            )
            author.fullname = author.fullname()
            author.save()
            self.stdout.write(f'{author.full_name}')