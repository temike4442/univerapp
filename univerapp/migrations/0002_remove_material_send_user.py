# Generated by Django 4.0.1 on 2022-05-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='send_user',
        ),
    ]