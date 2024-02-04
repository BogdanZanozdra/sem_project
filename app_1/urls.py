from django.urls import path
from .views import index, heads_tailes, dice, rand_number, authors_view, posts_view, about, heads_tailes_templ, \
    dice_templ, rand_number_templ, get_author_posts, get_post, choose_game, author_add, post_add

urlpatterns = [
    path('', index, name='index'),
    path('heads_tailes/', heads_tailes, name='heads_tailes'),
    path('heads_tailes_templ/<int:count>/', heads_tailes_templ, name='heads_tailes_templ'),
    path('dice/', dice, name='dice'),
    path('dice_templ/<int:count>/', dice_templ, name='dice_templ'),
    path('rand_number/', rand_number, name='rand_number'),
    path('rand_number_templ/<int:count>/', rand_number_templ, name='rand_number_templ'),
    path('authors/', authors_view, name='authors'),
    path('posts/', posts_view, name='posts'),
    path('get_post/<post_id>/', get_post, name='get_post'),
    path('author_posts/<int:author_id>/', get_author_posts, name='get_author_posts' ),
    path('about/', about, name='about'),
    path('game/', choose_game, name='game'),
    path('author/', author_add, name='author_add'),
    path('post/', post_add, name='post')
]
