from django.http import HttpResponse
from django.shortcuts import render, reverse
import time
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = str(time.strftime("%H:%M"))
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    working_directory = os.listdir(path='.')
    result = ', '.join(working_directory)
    msg = f'Содержимое рабочей директории: {result}'
    return HttpResponse(msg)
