from django.urls import path
from .views import *

urlpatterns = [
    path('', ResumeListView.as_view()),
    path('<int:pk>/', ResumeView.as_view()),
    path('create/', ResumeCreatView.as_view())
]
