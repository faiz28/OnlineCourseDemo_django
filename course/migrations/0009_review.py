# Generated by Django 3.0.5 on 2020-05-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_all_lesson_permision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('course_id', models.IntegerField()),
                ('summary', models.CharField(max_length=250)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
