# Generated by Django 3.2.8 on 2021-10-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='approved',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default='No'),
        ),
    ]
