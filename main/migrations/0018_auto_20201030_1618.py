# Generated by Django 3.1 on 2020-10-30 14:18

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201030_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modificateduser',
            name='number',
            field=phone_field.models.PhoneField(blank=True, default=1, max_length=31, unique=True, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
