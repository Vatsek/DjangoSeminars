from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birth_date = models.DateField()
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.full_name)

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
