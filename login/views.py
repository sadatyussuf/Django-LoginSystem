from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CreateUserForm,AuthenticateUserForm
from django.contrib import messages


def indexView(request):
    return render(request,'indexPage.html')


def SignUpView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Accout created successful')
            return redirect('login')
    else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = CreateUserForm()
    return render(request,'register.html',{'form':form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticateUserForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password.")
        else:
                messages.error(request,"Invalid username or password.")
    form = AuthenticateUserForm()

    return render(request,'loginPage.html',{'form':form})