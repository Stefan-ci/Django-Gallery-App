from django.contrib import admin
from gallery.models import Gallery, Image





class ImageAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'is_open_source', 'date']
    list_filter = ['is_open_source', 'date']
    search_fields = ['gallery__user__username', 'gallery__user__first_name', 'gallery__user__last_name', 'date', 'is_open_source']
    date_hierarchy = 'date'



class GalleryAdmin(admin.ModelAdmin):
    list_display = ['user', 'date']
    list_filter = ['date']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'date']
    date_hierarchy = 'date'







admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
