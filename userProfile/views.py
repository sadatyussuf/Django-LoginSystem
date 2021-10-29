from django.shortcuts import render, get_object_or_404
from .models import ProfileModel
from django.contrib.auth.models import User
# Create your views here.


def indexView(request, username):
    form = get_object_or_404(User, username=username)
    return render(request, 'userProfile/indexPage.html', {'form': form})
