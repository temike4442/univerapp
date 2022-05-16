# Generated by Django 4.0.1 on 2022-05-16 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('univerapp', '0011_remove_message_date_read_message_alter_message_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='send_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='send_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
