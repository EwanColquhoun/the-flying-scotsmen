# Generated by Django 3.2.8 on 2021-11-22 10:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0031_alter_contact_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]