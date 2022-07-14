from django import forms
from . import models


# create forms
class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = models.Reuniao

        fields = ['name',
                  'data',
                  'assunto']
        widgets = {
            'name': forms.TextInput(attrs={
                'label': 'Nome da Reunião:',
                'class': "form-control",
                'style': "max-width: 300px;font-family: 'Roboto', sans-serif;",
            }),
            'data': forms.DateTimeInput(attrs={
                'type': 'date',
                'class': "form-control",
                'placeholder': 'Insira a data da reunião'
            }),
            'assunto': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Assunto da Reuinião',
            })
        }


