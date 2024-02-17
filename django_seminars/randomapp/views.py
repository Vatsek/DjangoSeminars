from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import logging
from .models import Coin
import pandas as pd


MIN_NUM = 0
MAX_NUM = 100

logger = logging.getLogger(__name__)


def my_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Была вызвана функция {func.__name__}')
        return result
    return wrapper


@my_logger
def coin(request, n=None):
    side = ['орёл', 'решка']
    if n == None:
        result = random.choice(side)
        coin_new = Coin(side=result)
        coin_new.save()
        return HttpResponse(f'{result}')
    result_lst =[]
    for i in range(n):
        result = random.choice(side)
        result_lst.append(result)
        coin_new = Coin(side=result)
        coin_new.save()
    return render(request, 'randomapp/index.html', {'result':result_lst})


@my_logger
def coin_pd(request, n=None):
    side = ['орёл', 'решка']
    result_lst =[]
    for i in range(n):
        result = random.choice(side)
        result_lst.append({'Попытка': i + 1, 'результат': random.choice(side)})
        print(result_lst)
        coin_new = Coin(side=result)
        coin_new.save()
    df = pd.DataFrame(result_lst).to_html()
    return render(request, 'randomapp/index.html', {'result': df})



@my_logger
def dice(request, n=1):
    return HttpResponse(f' На кубике выпала цифра {random.randint(1, 6)}')
    result = []
    for i in range(n):
        result = random.randint(1, 6)
        result.append({'Попытка': i + 1, 'результат': result})
    df = pd.DataFrame(result).to_html()
    return render(request, 'randomapp/index.html', {'result': df})


@my_logger
def dice_pd(request, n=None):
    result = []
    for i in range(n):
        number = random.randint(1, 6)
        result.append({'Попытка': i + 1, 'результат': number})
    df = pd.DataFrame(result).to_html()
    return render(request, 'randomapp/index.html', {'result': df})


@my_logger
def random_num(request):
    return HttpResponse(f'Случайное число от {MIN_NUM} до {MAX_NUM} --> {random.randint(MIN_NUM, MAX_NUM)}')


def statistic(request, n):
    return JsonResponse(Coin.get_last_n_flip(n), json_dumps_params={'ensure_ascii': False})