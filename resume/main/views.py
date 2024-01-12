from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
import uuid
from .forms import AddPostForm, UploadFileForm
from django.core.paginator import Paginator
from .models import Categories, Resume, UploadFiles
from django.contrib.auth.decorators import login_required, permission_required


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить резюме", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    category = Categories.objects.all()

    contact_list = Resume.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/index.html', {'category': category, 'menu': menu, 'page_obj': page_obj})



def hanter(request, h_slug):
    post = get_object_or_404(Resume, slug=h_slug)
    return render(request, 'main/hanter.html', {'post': post})


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    contact_list = Resume.objects.filter(cat_id=category.pk)
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'title': f'Резюме: {category.name}',
        'page_obj': page_obj,
        'menu': menu,
    }
    return render(request, 'main/index.html', context=data)


@login_required
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'main/addpage.html', {'menu': menu, 'title': 'Добавление резюме', 'form': form})



@login_required
def about(request):
    
    contact_list = Resume.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/about.html',
                  {'title': 'О сайте', 'page_obj': page_obj,  'menu': menu})
 


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
     return HttpResponse('Авторизация')



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")