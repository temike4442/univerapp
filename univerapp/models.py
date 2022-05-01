from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name='Имя курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class User(AbstractUser):
    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        error_messages={
            'unique': ("Такой логин уже существует"),
        },
    )
    first_name = models.CharField('Имя', max_length=100, null=True)
    last_name = models.CharField('Фамилия', max_length=100, null=True)
    otchestvo = models.CharField('Отчество', max_length=100, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    number = models.CharField('Номер телефона', max_length=50, null=True)
    course = models.ManyToManyField(Course, related_name='student_course')
    is_student = models.BooleanField('Студент', default=False)
    is_teacher = models.BooleanField('Учитель', default=False)
    image = models.ImageField(verbose_name='Фото', upload_to='uploads/accounts/', blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class Student(User):

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(User):

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class Message(models.Model):
    send_user = models.OneToOneField(User,on_delete=models.SET_NULL,related_name='send_user',null=True)
    receiver_user = models.OneToOneField(User, on_delete=models.SET_NULL,related_name='receiver_user',null=True)
    date_message = models.DateTimeField('Дата',auto_now_add=True)
    title = models.CharField(max_length=200,blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'