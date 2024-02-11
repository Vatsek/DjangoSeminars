from django.urls import path
from . import views


urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('random_num/', views.random_num, name='random_num'),
    path('statistic/<int:n>', views.statistic, name='statistic'),
]
