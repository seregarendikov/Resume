from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
import uuid
from .forms import AddPostForm, UploadFileForm

from .models import Categories, Resume, UploadFiles



menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить резюме", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Resume.objects.all()
    category = Categories.objects.all()
    return render(request, 'main/index.html', {'posts':posts, 'category': category, 'menu': menu})



def hanter(request, h_slug):
    post = get_object_or_404(Resume, slug=h_slug)
    return render(request, 'main/hanter.html', {'post': post})


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Resume.objects.filter(cat_id=category.pk)

    data = {
        'title': f'Резюме: {category.name}',
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'main/index.html', context=data)



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




def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
#            handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
 
    return render(request, 'main/about.html', {'title': 'О сайте', 'menu': menu, 'form': form})
 


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
     return HttpResponse('Авторизация')



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")