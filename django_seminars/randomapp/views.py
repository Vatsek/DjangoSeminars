from django.shortcuts import render
from django.http import HttpResponse
import random
import logging


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
def coin(request):
    side = ['орёл', 'решка']
    return HttpResponse(f'{random.choice(side)}')

@my_logger
def dice(request):
    return HttpResponse(f'На кубике выпала цифра {random.randint(1, 6)}')


@my_logger
def random_num(request):
    return HttpResponse(f'Случайное число от {MIN_NUM} до {MAX_NUM} --> {random.randint(MIN_NUM, MAX_NUM)}')
