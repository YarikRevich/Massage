# Generated by Django 3.0.6 on 2020-08-26 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='made_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания услуги'),
            preserve_default=False,
        ),
    ]
