# Generated by Django 2.2.12 on 2020-05-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkash',
            name='username',
            field=models.CharField(default='', max_length=250),
        ),
    ]