from django.contrib import admin
from django.urls import path
from.import views


app_name = 'Meeting App'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
]
