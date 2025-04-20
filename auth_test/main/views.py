from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'main/home.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html', {'user': request.user})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')