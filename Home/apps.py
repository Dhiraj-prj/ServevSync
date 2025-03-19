from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Home'

def ready(self):
    import Home.signals  # Adjust the import based on your app structure
