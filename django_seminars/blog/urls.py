from django.urls import path
from . import views



urlpatterns = [
    path('posts/<int:author_id>/', views.get_posts, name='get_posts'),
    path('posts/post/<int:post_id>/', views.author_post, name='author_post'),
    path('author/author_form/', views.author_form, name='author_form'),
    path('post/', views.post_form, name='post_form'),
]
