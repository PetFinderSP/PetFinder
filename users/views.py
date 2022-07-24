from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        email = email.lower()
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not username.strip():
            print('O campo do nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo do email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=username, email=email, password=senha2)
        user.save()
        print('Usuário Criado com Sucesso!')
        return redirect('login')
    else:
        return render(request, 'users/cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        if username == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        user = auth.authenticate(request, username=username, password=senha)
        if user is not None:
            auth.login(request, user)
            
            return redirect('dashboard')
        else:
            print('Usuário ou senha inválidos')
            return redirect('login') 

        
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')