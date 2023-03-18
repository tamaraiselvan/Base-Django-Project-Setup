from django.apps import AppConfig


class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firstapp'

    # This signal is integrated in this app
    def ready(self):
        import firstapp.signals
