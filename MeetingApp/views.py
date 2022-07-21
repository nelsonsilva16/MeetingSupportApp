from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
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
    utilizador = models.User.objects.filter(participante__reuniao=id).values('username','participante__reuniao','participante__role','first_name','last_name')
    ficheiros = models.File.objects.filter(reuniao=id)
    votacoes = models.Votacao.objects.filter(reuniao=id).exclude(voto__participante=request.user)
    intervencoes = models.Intervencao.objects.filter(reuniao=id)


    reuniao = models.Reuniao.objects.filter(id= id)
    context = {'ficheiros': ficheiros,'participantes': utilizador, 'reuniao': reuniao,'votacoes': votacoes,'intervencoes': intervencoes}
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


def apagar_votacao(request, id, idreu):
    votos = models.Voto.objects.filter(votacao=id, voto=True).count()
    votos_contra = models.Voto.objects.filter(votacao=id , voto=False).count()
    votacao = models.Votacao.objects.get(id=id)
    models.Votacao.objects.get(id=id).delete()
    messages.success(request, ("{}: Votos a favor:{}/ Votos Contra:{}".format(votacao.assunto,votos,votos_contra)))
    return redirect('/reuniao/{}'.format(idreu))

def home(request):
    return render(request, 'MeetingApp/home.html', {})

def voto_favor(request,id,idreu):
    votacao = models.Votacao.objects.get(id=id)
    models.Voto.objects.create(votacao=votacao,participante=request.user,voto= True)
    return redirect('/reuniao/{}'.format(idreu))

def voto_contra(request,id,idreu):
    votacao = models.Votacao.objects.get(id=id)
    models.Voto.objects.create(votacao=votacao,participante=request.user,voto= False)
    return redirect('/reuniao/{}'.format(idreu))