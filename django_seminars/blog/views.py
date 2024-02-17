from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Comment
from django.http import HttpResponse


def get_posts(request, author_id):
    posts = Post.objects.filter(author_id=author_id)
    return render(request, 'blog/posts.html', {'posts': posts})


def author_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    # post = Post.objects.get(id=post_id) или так!
    post.views_count += 1
    post.save()
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/post.html', {'post':post, 'comments': comments})
