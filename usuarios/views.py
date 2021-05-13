from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.

def cadastro (request):
    if request.method == 'POST':
        nome = request.POST ['name']
        email = request.POST ['email']
        senha = request.POST ['password']
        senha2 = request.POST ['password2']
        if not nome.strip():
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request,'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()   
        messages.success(request, 'Cadastro realizado com sucesso! Utilize a outra aba para efetuar o login.')
        return redirect('login')
    else:
        return render(request,'cadastro.html')

def login (request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == "" or senha == "":
            messages.error(request,'Os campos email e senha não podem ficar em branco')
            return redirect('login')  
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso, Bem Vindo {} !'.format(user))
        return redirect ('dashboard')
    return render(request, 'login.html')
            

def dashboard(request):
    return render(request, 'dashboard.html')