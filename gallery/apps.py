from django.apps import AppConfig


class GalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'
    verbose_name = "Galerie"
    
    def ready(self):
        import gallery.signals
