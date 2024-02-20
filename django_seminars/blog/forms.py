from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        # fields = ['first_name', 'last_name', 'email', 'bio', 'birth_date'] так или как ниже, исключая те поля, которые не вводим сами
        exclude = ['full_name']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Почта', 'bio': 'Биография', 'birth_date':'Дата рождения'}


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField()
    # views_count = forms.IntegerField(initial=0)
    is_public = forms.BooleanField(required=False)


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    content = forms.CharField(widget=forms.Textarea)
