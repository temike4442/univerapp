from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from .models import *

@login_required(login_url='login/')
def home(request):
    return redirect('index')

class IndexView(ListView):
    model = User
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        if (self.request.user.is_teacher == True):
            context['courses'] = Course.objects.filter(teacher=self.request.user.pk)
        return context


class ChatsView(ListView):
    model = Dialog
    template_name = 'chatview.html'
    context_object_name = 'chats'

    def get_queryset(self):
        query = Dialog.objects.filter(Q(user1=self.request.user.pk)|Q(user2=self.request.user.pk))
        return query

class CourseView(ListView):
    model = User
    template_name = 'courseview.html'
    context_object_name = 'students'

    def get_queryset(self):
        course_object = self.kwargs.get('course_id')
        query = User.objects.filter(course__pk=course_object)
        return query

    def get_context_data(self,**kwargs):
        context = super(CourseView,self).get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs.get('course_id'))
        return context

class ChatView(ListView):
    model = Message
    template_name = 'chat.html'
    context_object_name = 'messages'

    def get_queryset(self):
        dialog_object = Dialog.objects.get(pk=self.kwargs.get('dialog_id'))
        receiver = dialog_object.user1.pk
        if(dialog_object.user1 == self.request.user):
            receiver = dialog_object.user2.pk
        query = Message.objects.filter(Q(send_user=self.request.user.pk) & Q(receiver_user=receiver)|Q(send_user=receiver) & Q(receiver_user=self.request.user.pk)).order_by('date_send_message')
        return query

    def get_context_data(self,**kwargs):
        context = super(ChatView,self).get_context_data(**kwargs)
        dialog_object = Dialog.objects.get(pk=self.kwargs.get('dialog_id'))
        receiver = dialog_object.user1
        if (dialog_object.user1 == self.request.user):
            receiver = dialog_object.user2
        context['receiver'] = receiver
        context['chats'] = Dialog.objects.filter(Q(user1=self.request.user.pk)|Q(user2=self.request.user.pk))
        return context

def send_message(request):
    if request.method=='POST':
        text = request.POST.get("message_text", "")
        send_to = request.POST.get("send_to", "")
        receiver_user = User.objects.get(pk=send_to)

        if len(request.FILES) != 0:
            image = request.FILES['image']
            Message.objects.create(send_user=request.user, receiver_user=receiver_user, title=text, file=image)
        else:
            Message.objects.create(send_user=request.user, receiver_user=receiver_user, title=text)
        return redirect('chats')
    else:
        return  redirect('chat/')

def edithometask(request,pk):
    if request.method=='POST':
        file = request.FILES['exec_file']
        HomeTask.objects.filter(pk=pk).update(exec_file=file)
        return redirect('chats')
    else:
        return  redirect('chat/')

def checkdialog(request,user_id):
    get_dialog = Dialog.objects.filter(Q(user1=request.user.pk) & Q(user2=user_id) |
                                    Q(user2=request.user.pk) & Q(user1=user_id))
    if get_dialog:
        pk_dialog = get_dialog.first().pk
        return HttpResponseRedirect(reverse('chat_id', kwargs={'dialog_id':pk_dialog}))
        #return reverse('hometasks', kwargs={'course_id': course})
    else:
        user_to = User.objects.get(pk=user_id)
        dialog_id = Dialog.objects.create(user1=request.user,user2=user_to)
        return HttpResponseRedirect(reverse('chat_id', kwargs={'dialog_id':pk_dialog}))


class MaterialsView(ListView):
    model = Material
    template_name = 'materialsview.html'
    context_object_name = 'materials'

    def get_queryset(self):
        course_object = self.kwargs.get('course_id')
        query = Material.objects.filter(course__pk=course_object)
        return query

    def get_context_data(self,**kwargs):
        context = super(MaterialsView,self).get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs.get('course_id'))
        return context

class HomeTaskView(ListView):
    model = HomeTask
    template_name = 'hometaskview.html'
    context_object_name = 'hometasks'

    def get_queryset(self):
        course_object = self.kwargs.get('course_id')
        query = HomeTask.objects.filter(course__pk=course_object,student=self.request.user.pk)
        return query

    def get_context_data(self,**kwargs):
        context = super(HomeTaskView,self).get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs.get('course_id'))
        return context

class HomeTaskDetailView(UpdateView):
    model = HomeTask
    pk_url_kwarg = 'hometask_id'
    template_name = 'hometaskdetailview.html'
    fields = ['exec_file', ]

    def get_success_url(self):
        course = self.kwargs.get('course_id')
        return reverse('hometasks', kwargs={'course_id': course})

    def get_context_data(self,**kwargs):
        context = super(HomeTaskDetailView,self).get_context_data(**kwargs)
        context['hometask'] = HomeTask.objects.get(pk=self.kwargs.get('hometask_id'))
        return context

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_object'

class MaterialCreateView(CreateView):
    model = Material
    template_name = 'materialcreateview.html'
    fields = ['title', 'file',]

    def get_success_url(self):
        course = self.kwargs.get('course_id')
        return reverse('materials', kwargs={'course_id': course})

    def get_context_data(self,**kwargs):
        context = super(MaterialCreateView,self).get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs.get('course_id'))
        return context
