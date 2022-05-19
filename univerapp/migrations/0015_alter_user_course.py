# Generated by Django 4.0.1 on 2022-05-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univerapp', '0014_remove_course_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, related_name='student_course', to='univerapp.Course'),
        ),
    ]
