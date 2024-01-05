from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
import uuid
from .forms import AddPostForm, UploadFileForm

from .models import Categories, Resume



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
        form = AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            # try:
            #     Resume.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления поста')
            form.save()
    else:
        form = AddPostForm()
    return render(request, 'main/addpage.html', {'menu': menu, 'title': 'Добавление резюме', 'form': form})


def handle_uploaded_file(f):
    name = f.name
    ext = ''
 
    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]
 
    suffix = str(uuid.uuid4())
    with open(f"uploads/{name}_{suffix}{ext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
 
    return render(request, 'main/about.html', {'title': 'О сайте', 'menu': menu, 'form': form})
 


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
     return HttpResponse('Авторизация')



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")