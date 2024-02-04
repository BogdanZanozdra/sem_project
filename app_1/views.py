from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from random import choice, randint
import logging
from .models import Coin, Author, Post
from .forms import GameType, AuthorForm, PostAddFormWidget

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'Главная страница'
    }
    logger.info('index get request')
    return render(request, 'app_1/index.html', context=context)


def about(request):
    context = {
        'name': 'Bogdan'
    }
    logger.info('about get request')
    return render(request, 'app_1/about.html', context=context)


def heads_tailes(request):
    result = choice(['eagle', 'number'])
    if result == 'eagle':
        res = 1
    else:
        res = 0
    logger.info(f'Coin side: {result}')
    coin = Coin(side=res)
    coin.save()
    data_dict = Coin.get_data(5)
    return HttpResponse(f'{result}, {data_dict}')


def heads_tailes_templ(request, count):
    result_list = []
    for i in range(count):
        result_list.append(choice(['eagle', 'number']))
    context = {
        'title': 'Орел или решка',
        'result_list': result_list,
    }
    return render(request, 'app_1/game.html', context=context)


def dice(request):
    result = randint(1, 6)
    logger.info(f'dice side: {result}')
    return HttpResponse(result)


def dice_templ(request, count):
    result_list = []
    for i in range(count):
        result_list.append(randint(1, 6))
    context = {
        'title': 'Кости',
        'result_list': result_list,
    }
    return render(request, 'app_1/game.html', context=context)


def rand_number(request):
    return HttpResponse(randint(0, 100))


def rand_number_templ(request, count):
    result_list = []
    for i in range(count):
        result_list.append(randint(1, 100))
    context = {
        'title': 'Случайное число от 1 до 100',
        'result_list': result_list,
    }
    return render(request, 'app_1/game.html', context=context)


def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)


def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)


def get_author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).all()
    context = {
        'posts': posts,
        'title': 'author posts'
    }
    return render(request, 'app_1/author_posts.html', context=context)


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'app_1/post.html', context={'post': post})


# def choose_game(request):
#     if request.method == 'POST':
#         form = GameType(request.POST)
#         if form.is_valid():
#             game_type = form.cleaned_data['game_type']
#             throw_number = form.cleaned_data['throw_number']
#             logger.info(f'{game_type}, {throw_number}')
#     else:
#         form = GameType()
#     return render(request, 'app_1/games.html', {'form': form})
def choose_game(request):
    if request.method == 'POST':
        form = GameType(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throw_number = form.cleaned_data['throw_number']
            logger.info(f'Получили {game_type=}, {throw_number=}.')
            if game_type == 'C':
                return heads_tailes_templ(request, throw_number)
            elif game_type == 'D':
                return dice_templ(request, throw_number)
            else:
                return rand_number_templ(request, throw_number)
    else:
        form = GameType()
    return render(request, 'app_1/games.html', {'form': form})


def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name, last_name=last_name, email=email, bio=bio, birthday=birthday)
            author.save()
            message = 'Author saved'
    else:
        form = AuthorForm()
        message = 'Fill the form'
    return render(request, 'app_1/post_form.html', {'form': form})


def post_add(request):
    if request.method == 'POST':
        form = PostAddFormWidget(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            is_published = form.cleaned_data['is_published']
            post = Post(title=title, content=content, publish_date=publish_date,
                        author=author, is_published=is_published)
            post.save()
            message = 'Author saved'
    else:
        form = PostAddFormWidget()
        message = 'Fill the form'
    return render(request, 'app_1/post_form.html', {'form': form, 'message': message})



