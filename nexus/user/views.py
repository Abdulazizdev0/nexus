from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print("USER", user)
            if user:
                login(request, user)
                return redirect('main')
    form = LoginForm()
    ctx = {
        "form": form
    }
    return render(request, 'login.html', ctx)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        print(form.is_valid(), request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = RegisterForm()
    ctx = {
        'form': form
    }
    return render(request, 'register.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('main')


