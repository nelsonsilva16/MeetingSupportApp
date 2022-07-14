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

    def str(self):
        return self.name


class Participante(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)

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

    def str(self):
        return self.name


class File(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='uploads', max_length=255)

    def str(self):
        return self.name


class Intervencao(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    datai = models.DateTimeField()
    dataf = models.DateTimeField()

    def str(self):
        return self.id


class Votacao(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    datai = models.DateTimeField()
    duracao = models.IntegerField()
    assunto = models.CharField(max_length=150)


class Presencas(models.Model):
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)







