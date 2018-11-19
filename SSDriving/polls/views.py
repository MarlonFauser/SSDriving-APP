from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')
