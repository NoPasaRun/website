from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserModel
import os
from django.conf import settings


admin.site.disable_action('delete_selected')


@admin.register(UserModel)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')
    actions = ['delete_user']

    def delete_user(self, request, queryset):
        for obj in queryset:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(obj.profile_photo)))
            User.objects.get(username=obj.user.username, password=obj.user.password).delete()
        queryset.delete()

    delete_user.short_description = 'Удалить пользователей'





