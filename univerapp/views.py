from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import *

@login_required(login_url='login/')
def home(request):
    return redirect('index')

class IndexView(ListView):
    model = User
    template_name = 'home.html'


class ChatsView(ListView):
    model = Dialog
    template_name = 'chatview.html'
    context_object_name = 'chats'

    def get_queryset(self):
        query = Dialog.objects.filter(Q(user1=self.request.user.pk)|Q(user2=self.request.user.pk))
        return query

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
        print(query)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dialog_object = Dialog.objects.get(pk=self.kwargs.get('dialog_id'))
        receiver = dialog_object.user1
        if (dialog_object.user1 == self.request.user):
            receiver = dialog_object.user2
        context['receiver'] = receiver
        print(receiver.image)
        return
