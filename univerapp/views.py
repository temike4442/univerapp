from django.contrib.auth.decorators import login_required
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
