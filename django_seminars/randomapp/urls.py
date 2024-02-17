from django.urls import path
from . import views


urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('coin/<int:n>', views.coin, name='coin'),
    path('coin_pd/<int:n>', views.coin_pd, name='coin_pd'),
    path('dice/', views.dice, name='dice'),
    path('dice_pd/<int:n>', views.dice_pd, name='dice_pd'),
    path('random_num/', views.random_num, name='random_num'),
    path('statistic/<int:n>', views.statistic, name='statistic'),
]
