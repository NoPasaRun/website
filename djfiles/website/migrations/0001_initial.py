# Generated by Django 2.2 on 2021-09-04 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add', to='user.UserModel', verbose_name='Создатель')),
            ],
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='user.UserModel', verbose_name='Лайкнул')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='website.AddModel', verbose_name='Объявление')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_content/')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='website.AddModel', verbose_name='Объявление')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, verbose_name='Коментарий')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='website.AddModel', verbose_name='Объявление')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='user.UserModel', verbose_name='Написал')),
            ],
        ),
    ]