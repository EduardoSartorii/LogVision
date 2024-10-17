from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_page(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirecione para a página inicial ou outra página
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
        
    return render(request, 'login.html')
