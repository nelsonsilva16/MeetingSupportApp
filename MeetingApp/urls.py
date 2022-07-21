from django.contrib import admin
from django.urls import path
from . import views
app_name = 'Meeting App'

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('Create_Reuniao/', views.criar_reuniao, name='Criar Reuniao'),
    path('Inicial', views.pagina_utilizador, name='Paginal Inicial'),
    path('reuniao/<str:id>',views.pagina_reuniao,name='Pagina Reuniao'),
    path('votacao/<str:id>',views.criar_votacao,name='Pagina Votacao'),
    path('delete/<str:id>/<str:idreu>',views.apagar_votacao,name='Apagar Votacao'),
    path('votoF/<str:id>/<str:idreu>',views.voto_favor),
    path('votoC/<str:id>/<str:idreu>',views.voto_contra),
    ]
