# Generated by Django 3.0.6 on 2020-08-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200821_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='photo',
            field=models.ImageField(default=1, upload_to='serviceimage/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
