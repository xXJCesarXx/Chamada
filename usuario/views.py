from django.shortcuts import render, redirect
from .forms import UsuarioForm

def criar_usuario(request):
    form = UsuarioForm(request.POST)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return redirect('index')

    return render(request, 'usuario/criar_usuario.html',{'form': form})