# Generated by Django 3.1 on 2020-09-04 20:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_visitimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]