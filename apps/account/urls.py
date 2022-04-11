from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/login/', login),
    path('auth/register/', register),
    path('resume/', include('apps.resume.urls')),
]
