import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse

def index_view(request):
    msg = (f"<a href={reverse('home')}>Main Page</a><br/>"
           f"<a href={reverse('time')}>Current date and time</a><br/>"
           f"<a href={reverse('workdir')}>Current directory</a>")
    return HttpResponse(msg)


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now()
    msg = f"Текущее время: {current_time}<br/><br/><a href={reverse('main')}>Back to index page</a><br/>"
    return HttpResponse(msg)


def workdir_view(request):
    dir_list = f"..<br>{'<br>'.join(os.listdir())}<br/><br/><a href={reverse('main')}>Back to index page</a>"
    msg = dir_list
    return HttpResponse(msg)

    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # raise NotImplemented
