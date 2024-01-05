from django.contrib import admin
from django.urls import include, path

from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('hanter/<slug:h_slug>', views.hanter, name='hanter'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
