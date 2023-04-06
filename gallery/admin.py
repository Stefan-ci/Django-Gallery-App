from django.contrib import admin
from gallery.models import Gallery, Image





class ImageAdmin(admin.ModelAdmin):
    list_display = ['gallery', 'is_open_source', 'is_deleted', 'date']
    list_filter = ['is_open_source', 'is_deleted', 'date']
    search_fields = ['gallery__user__username', 'gallery__user__first_name', 'gallery__user__last_name', 'date', 'is_open_source']
    date_hierarchy = 'date'



class GalleryAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'date']
    list_filter = ['is_active', 'date']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'date']
    date_hierarchy = 'date'







admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
