from django.contrib import admin
from .models import Author, Post, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'birth_date', 'full_name']
    list_filter = ['birth_date']
    fieldsets = (('Основная информация', {'fields': ['first_name', 'last_name', 'birth_date'],
                                          'description': 'В данной секции представлена основная информация пользователя',
                                          'classes': ['test', 'collapse'], # для добпвления класса css
                                        }
                  ),
                 ('Дополнительная информация', {'fields': ['email', 'bio']}),)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'views_count', 'is_public']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'author', 'create_date', 'edit_date']


