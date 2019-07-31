from django.shortcuts import render
from conta.models import Titular, Conta
from conta.rand import gerar_numero

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    if request.method == 'POST':

        try:
            titular = Titular()
            
            titular.nome = request.POST['nome']
            titular.sobrenome = request.POST['sobrenome']
            titular.data_nascimento = request.POST['nascimento']
            titular.cpf = request.POST['cpf']
            titular.email = request.POST['email']
            titular.senha = request.POST['senha']
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