# Generated by Django 3.2.8 on 2022-01-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
