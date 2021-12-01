# Generated by Django 3.2.8 on 2021-12-01 10:43

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg', models.CharField(max_length=6)),
                ('desc', models.CharField(max_length=25)),
                ('aircraft_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(help_text='Include country code, eg +44', max_length=128, region=None)),
                ('email', models.EmailField(help_text='Email must include "@"', max_length=40)),
                ('message', models.TextField()),
                ('replied', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=11, unique=True)),
                ('start', models.TimeField()),
                ('duration', models.TimeField()),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='Group_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='', help_text='Required, Why do you want to join The Flying Scotsmen?')),
                ('registered', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registered', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('instructor_requested', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=False, max_length=5)),
                ('notes', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=False)),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_aircraft', to='booking.aircraft')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.slot')),
            ],
            options={
                'ordering': ['date', 'slot'],
            },
        ),
    ]
