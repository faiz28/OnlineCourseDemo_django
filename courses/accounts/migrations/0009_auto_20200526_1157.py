# Generated by Django 2.2.12 on 2020-05-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200526_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='username',
            field=models.CharField(default='', max_length=250),
        ),
    ]