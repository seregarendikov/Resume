
from resume import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from main.views import page_not_found





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = page_not_found

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Панель администрирования'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)