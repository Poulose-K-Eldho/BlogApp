# Generated by Django 3.2.4 on 2021-06-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_remove_blogs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='img',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]
