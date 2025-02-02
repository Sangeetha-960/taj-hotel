# Generated by Django 5.0.6 on 2024-08-28 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=255)),
                ('cus_phone', models.CharField(max_length=10)),
                ('cus_email', models.EmailField(max_length=254)),
                ('book_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsix.rooms')),
            ],
        ),
    ]
