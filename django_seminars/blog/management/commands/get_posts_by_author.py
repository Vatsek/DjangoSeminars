from django.core.management.base import BaseCommand
from ...models import Author, Post
from django.utils import lorem_ipsum
from random import choice, randint


class Command(BaseCommand):
    help = 'Search all posts by author'

    def add_arguments(self, parser):
        parser.add_argument('author_name', type=str, help='User ID')


    def handle(self, *args, **kwargs):
        author_name = kwargs['author_name']
        print(author_name)
        posts = Post.objects.filter(author__first_name__icontains=author_name)

        # for post in posts:
        #     print(post.title)
        return str(posts)
