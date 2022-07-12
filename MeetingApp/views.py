from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from MeetingApp.forms import LoginForm, RegisterForm


#def register_view(request):
#    if request.method == 'POST':
#        form = RegisterForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('')
#        else:
#            form = RegisterForm()
#

def register_view(request):
    form_class = RegisterForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect('MeetingApp/register')

    return render(request, "MeetingApp/register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            return redirect('')
    else:
        form = LoginForm()
    return render(request, 'MeetingApp/login.html', {'form': form})