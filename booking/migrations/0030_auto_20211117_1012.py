# Generated by Django 3.2.8 on 2021-11-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0029_auto_20211104_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='slot',
            name='slot',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
