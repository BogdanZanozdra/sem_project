import datetime

from django import forms
from .models import Author, Post


class GameType(forms.Form):
    game_type = forms.ChoiceField(choices=[('C', 'coins'), ('D', 'dice'), ('N', 'numbers')])
    throw_number = forms.IntegerField(min_value=1, max_value=64)


# class AuthorForm(forms.Form):
#     name = forms.CharField()
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     bio = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today())


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email', 'bio', 'birthday']

# Или:

# Аналогично автору создайте форму добавления новой статьи. Автор статьи должен
# выбираться из списка (все доступные в базе данных авторы).


class PostAddFormWidget(forms.Form):
    title = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите заголовок статьи'}))
    content = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите текст статьи'}))
    publish_date = forms.DateTimeField(initial=datetime.datetime.now,
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    is_published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs=
                                                                                 {'class': 'form-check-input'}))
# Или:


# class PostAddFormWidget(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'category', 'views', 'is_published']
#
#     publish_date = forms.DateField(initial=datetime.date.today,
#                                    widget=forms.DateInput(attrs={
#                                     'class': 'form-control',
#                                     'type': 'date' # теперь календарь
#                                     }))
#     author = forms.ModelChoiceField(queryset=Author.objects.all().order_by('last_name'))
#
#

