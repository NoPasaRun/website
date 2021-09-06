from django.db import models
from user.models import UserModel


class AddModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Создатель', related_name='adds')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} {self.description[:15]}..."


class ImageModel(models.Model):
    add = models.ForeignKey(AddModel, on_delete=models.CASCADE, verbose_name='Объявление', related_name='images')
    image = models.ImageField(upload_to='user_content/')
    description = models.TextField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f"{self.description[:15]}..."


class CommentModel(models.Model):
    article = models.ForeignKey(AddModel, on_delete=models.CASCADE, verbose_name='Объявление', related_name='comments')
    text = models.TextField(max_length=100, verbose_name='Коментарий')
    writer = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Написал', related_name='comments')

    def __str__(self):
        return f"{self.writer} {self.text[:10]}..."
