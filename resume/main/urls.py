from django.contrib import admin
from django.urls import include, path

from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('hanter/<slug:h_slug>', views.hanter, name='hanter'),
]
