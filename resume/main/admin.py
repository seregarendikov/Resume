from django.contrib import admin
from .models import Categories, Resume


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'is_published')
    list_display_links = ('id', 'name')
    ordering = ['time_create']



admin.site.register(Resume, ResumeAdmin)
admin.site.register(Categories)