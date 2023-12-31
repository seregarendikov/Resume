
from django.db import models
from django.urls import reverse


class Resume(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    date = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    telephon_number = models.CharField(max_length=255)
    emeil = models.EmailField()
    profession = models.CharField(max_length=255)
    payment = models.CharField(max_length=255)
    competencies = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


    def get_absolute_url(self):
        return reverse('hanter', kwargs={'h_slug': self.slug})
    


class Categories(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})    
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')
