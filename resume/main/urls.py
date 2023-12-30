from django.contrib import admin
from django.urls import include, path

from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('hanter/<int:h_id>', views.hanter, name='hanter'),
]
