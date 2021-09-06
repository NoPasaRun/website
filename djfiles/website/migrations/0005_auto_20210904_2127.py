# Generated by Django 2.2 on 2021-09-04 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210904_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmodel',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adds', to='user.UserModel', verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.AddModel', verbose_name='Объявление'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.UserModel', verbose_name='Написал'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.AddModel', verbose_name='Объявление'),
        ),
        migrations.AlterField(
            model_name='likemodel',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='user.UserModel', verbose_name='Лайкнул'),
        ),
        migrations.AlterField(
            model_name='likemodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='website.AddModel', verbose_name='Объявление'),
        ),
    ]
