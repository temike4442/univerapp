from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name='Имя курса')
    teacher = models.ForeignKey('Teacher',on_delete=models.SET_NULL,null=True,blank=True,related_name='teacher_course')

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
    course = models.ManyToManyField(Course, related_name='student_course',blank=True)
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
    send_user = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='send_user',null=True)
    receiver_user = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='receiver_user',null=True)
    date_send_message = models.DateTimeField('Дата отправки',auto_now_add=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class Dialog(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='dialog_user1')
    user2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='dialog_user2')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    last_message_date = models.DateTimeField(null=True,blank=True)
    unread_message_user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Material(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course_materials')
    date_send_message = models.DateTimeField('Дата отправки', auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=False)

    class Meta:
        verbose_name = 'Обучающий материал'
        verbose_name_plural = 'Обучающий материалы'

class HomeTask(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='hometask_materials')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='hometask_send_user', null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='hometask_receiver_user',
                                         null=True)
    date_send_task = models.DateTimeField('Дата отправки', auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=False)
    is_exec = models.BooleanField(default=False)
    exec_date = models.DateTimeField(null=True,blank=True)
    exec_file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    status = models.CharField('Статус',default='ожидает ответа',max_length=60)

    class Meta:
        verbose_name = 'Тапшырма'
        verbose_name_plural = 'Тапшырмалар'