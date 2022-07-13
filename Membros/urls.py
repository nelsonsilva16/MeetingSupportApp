from django.contrib import admin
from django.urls import path
from.import views


app_name = 'Meeting App'

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
]