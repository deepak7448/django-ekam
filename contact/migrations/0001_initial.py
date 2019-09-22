# Generated by Django 2.2.5 on 2019-09-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(default='email', max_length=100)),
                ('subjects', models.CharField(default='subject', max_length=200)),
                ('messages', models.TextField(default='message')),
            ],
        ),
    ]