from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect(request, 'account/login.html')
    else:
        return render(request,'account/login.html')
