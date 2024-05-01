from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:dashboard')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
                print("Authentication failed")
        else:
            messages.error(request, 'Form validation failed.')
            print('Form not valid')
            print(form.error_messages)
    context = {'form': form}
    return render(request, 'login.html', context=context)


def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:dashboard')
            else:
                print('Authentication failed')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'register.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('main:home')