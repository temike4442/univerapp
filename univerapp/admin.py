from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .forms import StudentUserCreationForm,TeacherUserCreationForm

from .models import *

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
                'last_name', 'first_name', 'otchestvo', 'username', 'password','user_permissions', 'birthday', 'address', 'email',
                'is_student', 'is_teacher',
                'number', 'image')
        }),)

class HomeTaskAdmin(ModelAdmin):
    model = HomeTask
    list_display = ('title','student','date_send_task','status','course')
    list_filter = ('status','course__name',)

    def save_model(self, request, obj, form, change):
        if obj.is_exec == True:
            obj.status = 'Аткарылды'
        if obj.exec_file == '':
            obj.status = 'Кайра аткарууга жөнөтүлдү'
        super().save_model(request, obj, form, change)

class AnswerInline(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerInline]
    list_display = ['question','quiz']

class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    #inlines = [QuestionAdmin]


admin.site.register(User,MyUserAdmin)
admin.site.register(Course)
admin.site.register(Message)
admin.site.register(Dialog)
admin.site.register(Material)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Answer,AnswerInline)
admin.site.register(HomeTask,HomeTaskAdmin)
admin.site.register(Student, CustomUserAdmin)
admin.site.register(Teacher, TeacherUserAdmin)