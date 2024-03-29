from django.shortcuts import render,redirect
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        # Verificar se o usuário já existe pelo nome
        usuario_existente = Usuario.objects.filter(nome=nome).first()
        
        if usuario_existente:
            usuario_existente.idade = idade
            usuario_existente.save()
            
        else:
            if nome and idade:
                novo_usuario = Usuario(nome=nome, idade=idade)
                novo_usuario.save()
        
        return redirect('usuarios')
    else:
        usuarios = {'usuarios': Usuario.objects.all()}
        return render(request,'usuarios/usuarios.html',usuarios)


