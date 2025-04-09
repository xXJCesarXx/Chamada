from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES=[
        ('Administrador', 'Administrador'),
        ('Funcionários', 'Funcionários'),
        ('Sócio', 'Sócio')
    ]

    class Meta():
        model = User
        fields = ['username', 'email', 'last_name', 'first_name',]
    username = forms.CharField(label='Matricula: ')
    email = forms.EmailField(label='E-mail: ')
    last_name = forms.CharField(label='Nome Completo: ')
    first_name = forms.ChoiceField(
        label='Status: ',
        choices=FIRST_NAME_CHOICES,
        widget=forms.Select(attrs={'class':'custom-select'}),
        initial='Sócio'
    )