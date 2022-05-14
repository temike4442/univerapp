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
        print(self.request.user)
        query = Dialog.objects.filter(Q(user1=self.request.user.pk)|Q(user2=self.request.user.pk))
        print(query)
        return query

