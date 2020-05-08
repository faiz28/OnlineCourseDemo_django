# Generated by Django 3.0.5 on 2020-05-08 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bkash',
            name='date_subscribed',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='bkash',
            name='mobile_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
