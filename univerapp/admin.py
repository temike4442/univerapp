from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .forms import StudentUserCreationForm,TeacherUserCreationForm

from .models import User,Student,Teacher,Course,Message,Material,HomeTask,Dialog

class MyUserAdmin(UserAdmin):
    list_display = ['last_name', 'first_name', 'birthday', 'username', 'email', 'password', ]

class CustomUserAdmin(UserAdmin):
    add_form = StudentUserCreationForm
    model = Student
    list_display = ['last_name', 'first_name','birthday','username','email', 'password',]
    list_display_links = ['last_name', 'first_name','username',]
    fieldsets = (
        (None, {
            'fields': (
            'last_name', 'first_name', 'otchestvo', 'username', 'password', 'birthday','address','email', 'is_student', 'is_teacher',
            'number','course', 'image')
        }),)

class TeacherUserAdmin(UserAdmin):
    add_form = TeacherUserCreationForm
    model = Teacher
    list_display = ['last_name', 'first_name','birthday','username','email', 'password',]
    list_display_links = ['last_name', 'first_name', 'username', ]
    fieldsets = (
        (None, {
            'fields': (
                'last_name', 'first_name', 'otchestvo', 'username', 'password', 'birthday', 'address', 'email',
                'is_student', 'is_teacher',
                'number', 'image')
        }),)

class HomeTaskAdmin(ModelAdmin):
    model = HomeTask
    list_display = ('title','student','date_send_task','status')
    list_filter = ['status',]

    def save_model(self, request, obj, form, change):
        if obj.is_exec == True:
            obj.status = 'Аткарылды'
        super().save_model(request, obj, form, change)

admin.site.register(User,MyUserAdmin)
admin.site.register(Course)
admin.site.register(Message)
admin.site.register(Dialog)
admin.site.register(Material)
admin.site.register(HomeTask,HomeTaskAdmin)
admin.site.register(Student, CustomUserAdmin)
admin.site.register(Teacher, TeacherUserAdmin)