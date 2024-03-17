from django.shortcuts import render

# Create your views here.
# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'ice_cream/index.html'
    return render(request, template)


def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')