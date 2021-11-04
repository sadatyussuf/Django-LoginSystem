from django.urls import path
from .views import indexView, profileFormView

urlpatterns = [
    path('home/<int:pk>', indexView, name='index'),
    path('profile', profileFormView, name='profile')
]
