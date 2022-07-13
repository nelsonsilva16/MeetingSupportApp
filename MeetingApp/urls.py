from django.contrib import admin
from django.urls import path, include
from.import views


app_name = 'Meeting App'

urlpatterns = [
    path('home/', views.home, name='home'),
]
