# Generated by Django 5.0.6 on 2024-08-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=100)),
                ('room_rate', models.TextField()),
                ('room_img', models.ImageField(upload_to='abc')),
            ],
        ),
    ]