from django.apps import AppConfig


class WardrobeManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wardrobe_manager'

    def ready(self):
        import wardrobe_manager.signals 