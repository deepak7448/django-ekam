# Generated by Django 2.2.5 on 2019-09-20 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feedback',
        ),
    ]