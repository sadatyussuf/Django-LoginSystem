from django.urls import path
from .views import indexView

urlpatterns = [
    path('home/<str:username>',indexView,name='index'),
]