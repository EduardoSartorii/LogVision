from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')  
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')  
            messages.error(request, 'Nome de usuário ou senha inválidos.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')
