# Generated by Django 4.0.1 on 2022-05-18 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univerapp', '0013_alter_user_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='steps',
        ),
    ]
