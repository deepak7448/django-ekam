# Generated by Django 2.2.5 on 2019-09-20 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
    ]
