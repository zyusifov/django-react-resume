from django.urls import path
from .views import *

urlpatterns = [
    path('all/', ResumeListView.as_view()),
    path('<int:pk>/', ResumeView.as_view()),
    path('user/<int:pk>/', UserResumeView.as_view({'get': 'list'})),
    path('create/', ResumeCreateView.as_view())
]
