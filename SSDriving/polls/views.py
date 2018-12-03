from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    logger.warn(str(request.user))
    return render(request, 'home.html', {"home": "active"})


def contact(request):
    if request.method == 'POST':
        form = request.POST
        contactButton = form.get('contact', None)
        if contactButton != None:
            firstname = form.get('firstname', None)
            lastname = form.get('lastname', None)
            email = form.get('email', None)
            comment = form.get('comment', None)

            send_mail(
                subject='SSDriving recebeu seu contato! ' + firstname,
                from_email='ssdrivingsystem@gmail.com',
                recipient_list=[email],
                fail_silently=False,
                message='',
                html_message='Olá!<br/><br/> Ficamos felizes em receber seu contato, em breve um de nossos especialistas irá respondê-lo.<br/>Obrigado!<br/><br/> Att,<br/>Equipe SSDriving'
            )

            send_mail(
                subject='Contato recebido de ' + firstname,
                from_email='ssdrivingsystem@gmail.com',
                recipient_list=['ssdrivingsystem@gmail.com'],
                fail_silently=False,
                message='',
                html_message='<b>Contator:</b> ' + firstname + ' ' + lastname +
                    '<br/><br/><b>Comment:</b><br/>' + comment + '<br/><br/> Email: ' + email
            )
            return render(request, 'contact.html', {"contato": "active", "message": "Mensagem enviada com sucesso!"})
    return render(request, 'contact.html', {"contato": "active"})

@login_required
def logout(request):
    auth_logout(request)
    return render(request, 'home.html', {"home": "active"})

def login(request):
    if request.method == 'POST':
        form = request.POST
        loginButton = form.get('login', None)
        registerButton = form.get('register', None)

        if loginButton != None:
            username = form.get('username', None)
            password = form.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, 'home.html', {"username": username, "home": "active"})
            else:
                return render(request, 'login.html', {"loginerrormessage": "Usuário ou senha incorretos. Tente novamente!", "login": "active"})

        elif registerButton != None:
            username = form.get('username', None)
            email = form.get('email', None)
            password = form.get('password', None)
            # confirmPassword = form.get('confirmPassword', None)

            user, created = User.objects.get_or_create(
                username=username, email=email)
            if created:
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                auth_login(request, user)
                return render(request, 'home.html', {"username": username, "home": "active"})
            else:
                return render(request, 'login.html', {"registererrormessage": "O usuário que você está tentando cadastrar já existe. Tente novamente!", "login": "active"})
    return render(request, 'login.html', {"login": "active"})
