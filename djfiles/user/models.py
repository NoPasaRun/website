from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import cv2


class UserModel(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photos/', verbose_name='Фото профиля')
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100, verbose_name='Описание', blank=True)

    def __str__(self):
        return f"{self.user}"

    def save(self, *args, **kwargs):
        super(UserModel, self).save(*args, **kwargs)

        path = settings.MEDIA_ROOT + str(self.profile_photo)
        output = cv2.resize(cv2.imread(path), (128, 128))

        cv2.imwrite(path, output)
