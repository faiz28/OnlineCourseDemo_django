# Generated by Django 3.0.5 on 2020-05-07 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alllesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alllesson',
            old_name='les_Num',
            new_name='course_num',
        ),
        migrations.RenameField(
            model_name='alllesson',
            old_name='cou_num',
            new_name='lesson_Num',
        ),
    ]
