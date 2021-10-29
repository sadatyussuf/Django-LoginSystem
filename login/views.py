from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import CreateUserForm, AuthenticateUserForm
from django.contrib import messages


def SignUpView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accout created successful')
            return redirect('login')
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")
    else:
        form = CreateUserForm()

    return render(request, 'register.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticateUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index', username=username)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticateUserForm()

    return render(request, 'loginPage.html', {'form': form})


def logoutView(request):
    # if request.method == 'POST':
    logout(request)
    return redirect('login')
