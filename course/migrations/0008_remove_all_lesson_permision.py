# Generated by Django 3.0.5 on 2020-05-08 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20200508_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_lesson',
            name='permision',
        ),
    ]
