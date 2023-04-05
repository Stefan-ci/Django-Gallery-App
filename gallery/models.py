from django.db import models
from django.contrib.auth.models import User




class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ['-date']
    
    
    def __str__(self):
        return f"Gallery of {self.user.username}"






class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%Y/%m/')
    is_open_source = models.BooleanField(default=False, help_text="Check if you want to share this picture with everyone")
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
        ordering = ['-date', 'gallery']


    def __str__(self):
        return f"Picture of {self.gallery.user.username}"
    




