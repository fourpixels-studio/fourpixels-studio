from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def account_logout(request):
    logout(request)
    return redirect('account_login')


def account_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back 4hunnid!')
                return redirect('index')
            else:
                messages.info(request, 'Username Or Password is incorrect')

    context = {
        'title_tag': "Log In",
    }

    return render(request, 'account_login.html', context)
