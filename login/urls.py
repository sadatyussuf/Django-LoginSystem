from django.urls import path
from .views import SignUpView,loginView,indexView
urlpatterns = [
    path('',indexView,name='index'),
    path('signup/',SignUpView,name='signup'),
    path('login/',loginView,name='login'),
]