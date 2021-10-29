from django.urls import path
from .views import SignUpView,loginView,logoutView
urlpatterns = [
    
    path('signup/',SignUpView,name='signup'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
]