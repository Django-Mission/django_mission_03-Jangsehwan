from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm, SignUpForm, LoginFrom



def signup_view(request):
    # GET요청시 HTML응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts/signup.html')


def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.user_cache)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
