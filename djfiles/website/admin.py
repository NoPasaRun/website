from django.contrib import admin
from .models import AddModel, ImageModel, CommentModel
from django.conf import settings
import os


@admin.register(AddModel)
class AddAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'title']
    actions = ['delete_add']

    def delete_add(self, request, queryset):
        for add in queryset:
            for image in add.images.all():
                os.remove(os.path.join(settings.MEDIA_ROOT, str(image.image)))
        queryset.delete()

    delete_add.short_description = 'Удалить объявления'


@admin.register(ImageModel)
class AddAdmin(admin.ModelAdmin):
    list_display = ['id', 'add', 'description']
    actions = ['delete_image']

    def delete_image(self, request, queryset):
        for image in queryset:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(image.image)))
        queryset.delete()

    delete_image.short_description = 'Удалить изображения'


@admin.register(CommentModel)
class AddAdmin(admin.ModelAdmin):
    list_display = ['id', 'writer', 'article']