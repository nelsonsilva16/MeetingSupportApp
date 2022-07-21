from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class Utilizador(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=40)
#     password2 = models.CharField(max_length=40)
#
#     def str(self):
#         return self.project_name


class Reuniao(models.Model):
    name = models.CharField(max_length=255)
    data = models.DateTimeField()
    assunto = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Participante(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)

    PRES = 'Presidente'
    VP = 'Vice-presidente'
    SECRET = 'Secretário'
    PART = 'Participante'

    Roles = [
        (PRES,'Presidente'),
        (VP, 'Vice-Presidente'),
        (SECRET, 'Secretário'),
        (PART, 'Participante'),
    ]
    role = models.CharField(
        max_length=20,
        choices=Roles,
        default=PART,
    )

    def __str__(self):
        return self.name



class File(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='uploads', max_length=255)

    def __str__(self):
        return self.name


class Intervencao(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    participante = models.ForeignKey(User, on_delete=models.CASCADE)
    datai = models.DateTimeField()
    def __str__(self):
        return self.reuniao.name


class Votacao(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=150)
    def __str__(self):
        return self.assunto

class Voto(models.Model):
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    participante = models.ForeignKey(User, on_delete=models.CASCADE)
    voto = models.BooleanField()
    def __str__(self):
        return self.votacao.assunto


class Presencas(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
    def __str__(self):
        return self.reuniao.name






