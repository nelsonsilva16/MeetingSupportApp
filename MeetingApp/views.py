from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . import models
from . import forms

def home(request):
    return render(request, 'MeetingApp/home.html', {})
# Create your views here.

def criar_reuniao(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = forms.ReuniaoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "MeetingApp/CriarReuniao.html", context)


def pagina_utilizador(request):
    reunioes = models.Reuniao.objects.all()
    context = {'reunioes': reunioes}
    return render(request, "MeetingApp/Initial_page.html", context)


def pagina_reuniao(request,id):
    utilizador = models.Utilizador.objects.filter(participante__reuniao=id).values('name','participante__role')
    ficheiros = models.File.objects.filter(reuniao=id)

    reuniao = models.Reuniao.objects.filter(id=id)
    context = {'ficheiros': ficheiros,'participantes': utilizador,'reuniao':reuniao}
    return render(request, "MeetingApp/ReuniaoPage.html", context)


def criar_documentos(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = forms.ReuniaoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "MeetingApp/CriarReuniao.html", context)

# def createProject(response):
#     form = ProjectForm
#     if response.method == 'POST':
#         form = ProjectForm(response.POST, response.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Index')
#     context = {'form': form}
#     return render(response, 'DigitalHubApp/create_project.html', context)
