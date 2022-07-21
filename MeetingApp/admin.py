from django.contrib import admin
from MeetingApp import models
# Register your models here.
admin.site.register(models.Reuniao)
admin.site.register(models.File)
admin.site.register(models.Participante)
admin.site.register(models.Intervencao)
admin.site.register(models.Votacao)
admin.site.register(models.Voto)
