from django.urls import path
from .views import *

urlpatterns = [
    path('auth/login/', login),
    path('auth/register/', register),
]
