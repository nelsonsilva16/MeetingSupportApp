from django.contrib import admin
from django.urls import path
from . import views
app_name = 'Meeting App'

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('Create_Reuniao/', views.criar_reuniao, name='Criar Reuniao'),
    path('Inicial', views.pagina_utilizador, name='Paginal Inicial'),
    path('reuniao/<str:id>',views.pagina_reuniao,name='Pagina Reuniao'),]
