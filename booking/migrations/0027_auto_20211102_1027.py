# Generated by Django 3.2.8 on 2021-11-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_contact_replied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='maverick@topgun.com', max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(help_text='Type you message here...'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(help_text='Including country code', max_length=20),
        ),
    ]