from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, help_text="Activate/Deactivate the current gallery")
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ['-date']
    
    
    def __str__(self):
        return f"Gallery of {self.user.username}"
    
    def get_absolute_url(self):
        return reverse('user-gallery', kwargs={})


    
    def images(self):
        return Image.objects.filter(gallery=self, is_deleted=False)
    
    def private_images(self):
        return Image.objects.filter(gallery=self, is_open_source=False, is_deleted=False)
    
    def public_images(self):
        return Image.objects.filter(gallery=self, is_open_source=True, is_deleted=False)
    
    def deleted_images(self):
        return Image.objects.filter(gallery=self, is_deleted=True)






class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/')
    is_open_source = models.BooleanField(default=False, help_text="Check if you want to share this picture with everyone")
    is_deleted = models.BooleanField(default=False, help_text="Deleted (deactivate) the current image")
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
        ordering = ['-date', 'gallery']


    def __str__(self):
        return f"Picture of {self.gallery.user.username}"
    




