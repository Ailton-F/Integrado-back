# Generated by Django 4.2.1 on 2023-06-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livresse', '0004_book_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='idName',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
