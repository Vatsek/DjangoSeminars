from django.core.management.base import BaseCommand
from ...models import Author, Post, Comment
from django.utils import lorem_ipsum
from random import choice, randint


class Command(BaseCommand):
    help = 'create comment'

    def handle(self, *args, **kwargs):
        for i in range(10):
            authors = Author.objects.all()
            posts = Post.objects.all()

            for i in range(10):
                comment = Comment(
                    author = choice(authors),
                    post = choice(posts),
                    content = '\n'.join(lorem_ipsum.paragraphs(3, common=False)),
                    create_date = f'2000-02-{randint(1, 28)}',
                    edit_date = f'2000-03-{randint(1, 30)}',
                )
                comment.save()
