from django.shortcuts import render

# Create your views here.
# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'ПОСТЫ ОТФИЛЬТРОВАННЫЕ ПО ГРУППАМ!!!!! {slug}') 