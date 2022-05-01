from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

from .models import User,Student,Teacher,Course,Message

class MyUserAdmin(UserAdmin):
    list_display = ['last_name', 'first_name', 'birthday', 'username', 'email', 'password', ]

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Student
    list_display = ['last_name', 'first_name','birthday','username','email', 'password',]
    list_display_links = ['last_name', 'first_name','username',]
    fieldsets = (
        (None, {
            'fields': (
            'last_name', 'first_name', 'otchestvo', 'username', 'password', 'birthday', 'is_student', 'is_teacher',
            'number', 'image')
        }),)

class TeacherUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Teacher
    list_display = ['last_name', 'first_name','birthday','username','email', 'password',]
    list_display_links = ['last_name', 'first_name', 'username', ]

admin.site.register(User,MyUserAdmin)
admin.site.register(Course)
admin.site.register(Message)
admin.site.register(Student, CustomUserAdmin)
admin.site.register(Teacher, TeacherUserAdmin)