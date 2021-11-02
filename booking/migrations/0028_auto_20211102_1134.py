# Generated by Django 3.2.8 on 2021-11-02 11:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0027_auto_20211102_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='maverick@topgun.com', max_length=40, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
