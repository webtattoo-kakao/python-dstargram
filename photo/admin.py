from django.contrib import admin

# Register your models here.

from .models import Photo



class PhotoAdmin(admin.ModelAdmin):

    list_display = ['id', 'author', 'created', 'updated']
    search_fields = ['text', 'created']
    list_filter = ['created', 'updated', 'author']
    ordering = ['-updated', '-created']
    raw_id_fields = ['author']




admin.site.register(Photo, PhotoAdmin)
