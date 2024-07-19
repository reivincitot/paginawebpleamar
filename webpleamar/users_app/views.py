from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página 'home' después del inicio de sesión
        else:
            messages.error(request, 'Credenciales inválidas. Inténtelo de nuevo.')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')