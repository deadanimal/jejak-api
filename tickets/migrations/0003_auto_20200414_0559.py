# Generated by Django 2.2.6 on 2020-04-14 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0002_auto_20200413_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='solved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_message_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_message_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
