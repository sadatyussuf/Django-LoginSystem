from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProfileModel
from django.contrib.auth.models import User
from .forms import CreateUserProfileForms
# Create your views here.


def indexView(request, pk):
    form = get_object_or_404(User, id=pk)
    profile = get_object_or_404(ProfileModel, user_id=pk)
    return render(request, 'userProfile/indexPage.html', {'form': form, 'profile': profile})


def profileFormView(request):
    if request.method == 'POST':
        form = CreateUserProfileForms(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            print(request.POST)
            current_user = request.user
            return redirect('index', pk=current_user.id)
    else:
        form = CreateUserProfileForms()
    return render(request, 'userProfile/profilePage.html', {'form': form})
