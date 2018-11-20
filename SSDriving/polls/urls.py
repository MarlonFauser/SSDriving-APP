from django.urls import path

from . import views

urlpatterns = [
    # ex: http://localhost:8000/
    path('', views.home, name='home'),
    # ex: http://localhost:8000/contato
    path('contato', views.contact, name='contato'),
    # ex: http://localhost:8000/login
    path('login', views.login, name='login'),
    # ex: http://localhost:8000/login
    path('accounts/', include('django.contrib.auth.urls')),
]
