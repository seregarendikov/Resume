from django import forms
from .models import Categories


class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label="ФИО", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    date = forms.CharField(max_length=255, label="Дата рождения")
    city = forms.CharField(max_length=255, label="Город")
    telephon_number = forms.CharField(max_length=255, label="Телефон")
    emeil = forms.CharField(max_length=255, label="Электронная почта")
    profession = forms.CharField(max_length=255, label="Должность")
    payment = forms.CharField(max_length=255, label="Желаемая зарплата")
    competencies = forms.CharField(widget=forms.Textarea(), label="Навыки")
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(), label="Категория")
    