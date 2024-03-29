# Generated by Django 2.2.5 on 2019-09-21 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190921_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='about_us',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=13),
            preserve_default=False,
        ),
    ]
