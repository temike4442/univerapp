from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name='Имя курса')
    steps = models.SmallIntegerField('Длительность курса в уроках',null=False,blank=False,default=10)

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
    email = models.EmailField('Email', max_length=100,null=True,blank=True)
    number = models.CharField('Номер телефона', max_length=50, null=True)
    address = models.CharField('Адрес', max_length=100, null=True)
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
    about = models.CharField('Немного о себе', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class Message(models.Model):
    send_user = models.OneToOneField(User,on_delete=models.SET_NULL,related_name='send_user',null=True)
    receiver_user = models.OneToOneField(User, on_delete=models.SET_NULL,related_name='receiver_user',null=True)
    date_send_message = models.DateTimeField('Дата отправки',auto_now_add=True,null=True)
    date_read_message = models.DateTimeField('Дата прочитания',null=True)
    title = models.CharField(max_length=200,blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Material(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course_materials')
    send_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='material_send_user', null=True)
    receiver_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='material_receiver_user', null=True)
    date_send_message = models.DateTimeField('Дата отправки', auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=False)

    class Meta:
        verbose_name = 'Обучающий материал'
        verbose_name_plural = 'Обучающий материалы'

class HomeTask(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='hometask_materials')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='hometask_send_user', null=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='hometask_receiver_user',
                                         null=True)

    date_send_task = models.DateTimeField('Дата отправки', auto_now_add=True)

    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=False)

    class Meta:
        verbose_name = 'Обучающий материал'
        verbose_name_plural = 'Обучающий материалы'