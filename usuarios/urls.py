from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
path('cadastro', views.cadastro, name='cadastro'),
path('login', views.login, name='login'),
path('dashboard', views.dashboard, name='dashboard')


]   