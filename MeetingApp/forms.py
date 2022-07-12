from django import forms

from.import models


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Utilizador

        fields = ['name',
                  'password',
                  ]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.Utilizador

        fields = ['name',
                  'email',
                  'password',
                  'password2',
                  ]

