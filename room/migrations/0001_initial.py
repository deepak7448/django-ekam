# Generated by Django 2.2.5 on 2019-09-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rooms/')),
                ('title', models.CharField(default='title', max_length=30)),
                ('description', models.TextField(default='description', max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'room',
            },
        ),
    ]