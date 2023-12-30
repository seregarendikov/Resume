from django.db import models


class Resume(models.Model):

    name = models.CharField(max_length=255)
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