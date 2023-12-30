from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Resume



data = [{'id': 1, 'name': 'Рендиков Сергей Сергеевич', 'date': '09.03.1986', 'city': 'Omsk', 'slug':'sergey-rendikov'},
        {'id': 2, 'name': 'Иванов Иван Иванович', 'date': '31.04.2000', 'city': 'Красноярск', 'slug':'sergey-rendikov'},
        {'id': 3, 'name': 'Сидоров Александр Дитриевич', 'date': '15.03.1980', 'city': 'Санкт-Петербург', 'slug':'sergey-rendikov'},]


def index(request):
    posts = Resume.objects.filter(is_published=1)
    return render(request, 'main/index.html', {'data': data, 'posts':posts})



def hanter(request, h_slug):
    post = get_object_or_404(Resume, slug=h_slug)
    return render(request, 'main/hanter.html', {'data': data, 'post': post})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")