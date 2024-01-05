from django.apps import AppConfig


class MainConfig(AppConfig):
    verbose_name = 'База данных'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
