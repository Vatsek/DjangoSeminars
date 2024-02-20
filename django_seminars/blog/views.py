from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment
from django.http import HttpResponse
from .forms import AuthorForm, PostForm, CommentForm


def get_posts(request, author_id):
    posts = Post.objects.filter(author_id=author_id)
    return render(request, 'blog/posts.html', {'posts': posts})


def author_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    # post = Post.objects.get(id=post_id) или так!
    post.views_count += 1
    post.save()
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(author = data['author'],
                                    post = post,
                                    content = data['content'])
            return redirect('author_post', post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/post.html', {'post':post, 'comments': comments, 'form': form})


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save() # так делается, когда форма создана на основе модели!!!! иначе не работает
            return redirect('author_form')
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(title=data['title'],
                                    content=data['content'],
                                    pub_date=data['pub_date'],
                                    author=data['author'],
                                    category=data['category'],
                                    is_public=data['is_public'])
            return redirect('post_form')
    else:
        form = PostForm()
    return render(request, 'blog/author_form.html', {'form': form})
