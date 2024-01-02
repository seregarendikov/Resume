from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Categories, Resume




def index(request):
    posts = Resume.objects.all()
    categor = Categories.objects.all()
    # cat = Categories.objects.all()
    return render(request, 'main/index.html', {'posts':posts, 'category': categor})



def hanter(request, h_slug):
    post = get_object_or_404(Resume, slug=h_slug)
    return render(request, 'main/hanter.html', {'post': post})


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Resume.objects.filter(cat_id=category.pk)

    data = {
        'title': f'Резюме: {category.name}',
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'main/index.html', context=data)



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")