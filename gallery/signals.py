from gallery.models import Gallery
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_gallery(sender, instance, created, **kwargs):
    if created:
        Gallery.objects.create(user=instance)
post_save.connect(create_gallery, sender=User)
