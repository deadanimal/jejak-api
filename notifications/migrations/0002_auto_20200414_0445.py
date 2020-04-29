# Generated by Django 2.2.6 on 2020-04-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='active',
        ),
        migrations.AddField(
            model_name='notification',
            name='created',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
