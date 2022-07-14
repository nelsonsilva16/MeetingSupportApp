from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . import forms, models
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
    utilizador = request.user
    reunioes = models.Reuniao.objects.filter(participante__name=utilizador.id)
    context = {'reunioes': reunioes}
    return render(request, "MeetingApp/Initial_page.html", context)


def pagina_reuniao(request,id):
    utilizador = models.User.objects.filter(participante__reuniao=id).values('username','participante__reuniao','participante__role')
    ficheiros = models.File.objects.filter(reuniao=id)

    reuniao = models.Reuniao.objects.filter(id= id)
    context = {'ficheiros': ficheiros,'participantes': utilizador, 'reuniao': reuniao}
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

def criar_votacao(request, id):
    context = {}
    reuniao = models.Reuniao.objects.get(id=id).id
    # add the dictionary during initialization
    form = forms.VotacaoForm(request.POST or None, initial={'reuniao': reuniao})

    if form.is_valid():

        form.save()
        return redirect('/reuniao/{}'.format(id))

    context['form'] = form
    return render(request, "MeetingApp/Criar_votacao.html", context)


def home(request):
    return render(request, 'MeetingApp/home.html', {})