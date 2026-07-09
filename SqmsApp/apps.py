from django.apps import AppConfig


class SqmsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SqmsApp'

    def ready(self):
        import SqmsApp.signals