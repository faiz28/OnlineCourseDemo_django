# Generated by Django 3.0.5 on 2020-05-07 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200507_1318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Allcourse',
            new_name='All_course',
        ),
        migrations.RenameModel(
            old_name='Alllesson',
            new_name='All_lesson',
        ),
        migrations.RenameField(
            model_name='all_lesson',
            old_name='course_num',
            new_name='course_Num',
        ),
    ]
