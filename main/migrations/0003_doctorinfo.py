# Generated by Django 3.0.6 on 2020-08-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_made_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField(max_length=1000, verbose_name='Про доктора')),
                ('work_time_1', models.CharField(max_length=18, verbose_name='Время роботы 1')),
                ('work_time_2', models.CharField(max_length=18, verbose_name='Время роботы 2')),
            ],
            options={
                'verbose_name': 'Информация про доктора',
                'db_table': 'about_doctor',
            },
        ),
    ]
