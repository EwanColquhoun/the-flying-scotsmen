# Generated by Django 3.2.8 on 2021-11-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_auto_20211028_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]