# Generated by Django 3.1.6 on 2021-05-06 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210505_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_dates',
        ),
    ]
