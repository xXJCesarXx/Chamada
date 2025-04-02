from django import forms
from chamadaApp.models import Categoria, Plano, Telefone, Cliente

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'