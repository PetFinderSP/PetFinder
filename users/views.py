from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        email = email.lower()
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo do nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo do email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.using('AWS').filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha2)
        user.save(using='AWS')
        print('Usuário Criado com Sucesso!')
        return redirect('login')
    else:
        return render(request, 'users/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.using('AWS').filter(email=email).exists():
            nome = User.objects.using('AWS').filter(email=email).values_list('username', flat=True).get()    
            print(nome)

        return redirect('dashboard')
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')