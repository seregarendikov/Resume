from django import forms
from .models import Categories, Resume


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="Категория не выбрана", label="Категории")
    # name = forms.CharField(max_length=255, label="ФИО", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # date = forms.CharField(max_length=255, label="Дата рождения")
    # city = forms.CharField(max_length=255, label="Город")
    # telephon_number = forms.CharField(max_length=255, label="Телефон")
    # emeil = forms.CharField(max_length=255, label="Электронная почта")
    # profession = forms.CharField(max_length=255, label="Должность")
    # payment = forms.CharField(max_length=255, label="Желаемая зарплата")
    # competencies = forms.CharField(widget=forms.Textarea(), label="Навыки")
    # is_published = forms.BooleanField()
    # cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label="Категория")
    

    class Meta:
    

        model = Resume
        fields = ['name', 'slug', 'date', 'city', 'telephon_number', 'emeil', 'profession', 'payment', 'competencies', 'is_published', 'cat']
        labels = {'slug': 'URL'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'competencies': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Изображение")   