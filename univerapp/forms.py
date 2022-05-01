from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Student,Teacher

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ('last_name', 'first_name', 'otchestvo', 'username', 'password', 'birthday', 'is_student', 'is_teacher', 'number','image')