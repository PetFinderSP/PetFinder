from re import U
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        email = email.lower()
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not username.strip():
            messages.error(request, 'O campo do nome não pode ficar em branco!')
            print('O campo do nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'o campo do email não pode ficar em branco!')
            print('O campo do email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais!')
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(username=username, email=email, password=senha2)
            user.save()
            messages.success(request, 'Usuário Cadastrado com Sucesso')
            print('Usuário Criado com Sucesso!')
            return redirect('login')
    else:
        return render(request, 'users/cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        if username == "" or senha == "":
            messages.error(request, 'Os campos usuário e senha não podem ficar em branco!')
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        user = auth.authenticate(request, username=username, password=senha)
        if user is not None:
            auth.login(request, user)
            
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            print('Usuário ou senha inválidos')
            return redirect('login') 

        
    return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html')
    else:
        return redirect('index')

def edita_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_id = request.POST['user_id']
            u = request.POST['username']
            e = request.POST['email']
            senha_nova = request.POST['password2']
            senha_nova2 = request.POST['password3']
            myuser = User.objects.get(pk=user_id)
            if not u.strip():
                messages.error(request, 'O campo do nome não pode ficar em branco!')
                print('O campo do nome não pode ficar em branco')
                return redirect('edita_user')
            if not e.strip():
                messages.error(request, 'o campo do email não pode ficar em branco!')
                print('O campo do email não pode ficar em branco')
                return redirect('edita_user')
            if senha_nova != senha_nova2:
                messages.error(request, 'As senhas não são iguais!')
                print('As senhas não são iguais')
                return redirect('edita_user')
            myuser.username=u
            myuser.email=e
            myuser.set_password(senha_nova2)
            myuser.save()
            messages.success(request, 'Atualizado com sucesso!')
            return redirect('login')

        return render(request,'users/edita_user.html')
    else:
        return redirect('login')