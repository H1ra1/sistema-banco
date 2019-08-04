from django.shortcuts import render, redirect
from conta.models import Perfil, Conta, User
from conta.rand import gerar_numero
from django.contrib.auth import authenticate, login
from conta.forms import RegisterForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
            username = user.username, 
            password = form.cleaned_data['password1']
            )
            login(request, user)
            print(form)
            return render(request, 'cadastrar.html')
    else:
        form = RegisterForm()

    ctx = {'form': form}
    return render(request, 'registrar.html', ctx)

@login_required
def cadastrar(request):
    if request.method == 'POST':

        try:
            titular = Perfil()
            user_id = request.POST['id']
            titular.user = User.objects.get(id = user_id)
            titular.nome = request.POST['nome']
            titular.sobrenome = request.POST['sobrenome']
            titular.data_nascimento = request.POST['nascimento']
            titular.cpf = request.POST['cpf']
            titular.telefone = request.POST['telefone']
            titular.genero = request.POST['genero']
            titular.save()

            conta = Conta()

            conta.titular = titular
            conta.numero_conta = gerar_numero()
            conta.save()
            return render(request, 'cadastrar.html', {'msg': 'Cadastro efetuado!'})
        except:
            print('error')
            return render(request, 'cadastrar.html', {'msg': 'Error'})
    
    return render(request, 'cadastrar.html')

