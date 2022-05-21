from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import HomeTask,Student,Teacher


class StudentUserCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'otchestvo', 'username', 'password', 'birthday', 'is_student', 'is_teacher', 'number','image')

class TeacherUserCreationForm(UserCreationForm):

    class Meta:
        model = Teacher
        fields = ('last_name', 'first_name', 'otchestvo','username', 'password', 'birthday', 'is_student', 'is_teacher', 'number','image')

class HomeTaskForm(forms.ModelForm):
    class Meta:
        model = HomeTask
        fields = ('title', 'file', 'is_exec','exec_file', )