# Generated by Django 3.1 on 2020-10-30 14:21

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20201030_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modificateduser',
            name='number',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='Номер телефона'),
        ),
    ]
