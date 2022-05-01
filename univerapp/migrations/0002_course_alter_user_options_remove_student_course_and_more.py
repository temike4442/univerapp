# Generated by Django 4.0.1 on 2022-04-30 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('univerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='course',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/accounts/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Учитель'),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=50, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='user',
            name='otchestvo',
            field=models.CharField(max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Такой логин уже существует'}, max_length=150, unique=True, verbose_name='Логин'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_message', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('file', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/')),
                ('receiver_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver_user', to=settings.AUTH_USER_MODEL)),
                ('send_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='send_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(related_name='student_course', to='univerapp.Course'),
        ),
    ]
