# Generated by Django 3.0.6 on 2020-05-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_allcourse_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alllesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('les_Num', models.IntegerField()),
                ('cou_num', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('link', models.URLField()),
            ],
        ),
    ]
