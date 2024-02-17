from django.urls import path
from . import views



urlpatterns = [
    path('posts/<int:author_id>/', views.get_posts, name='get_posts'),
    path('posts/post/<int:post_id>/', views.author_post, name='author_post'),
]
