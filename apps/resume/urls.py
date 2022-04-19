from django.urls import path
from .views import *

urlpatterns = [
    path('all/', ResumeListView.as_view()),
    path('user/<int:pk>/', UserResumeView.as_view({'get': 'list'})),
    path('create/', ResumeCreateView.as_view()),
    path('skill/', SkillView.as_view({'get': 'list'})),
    path('education/', EducationView.as_view({'get': 'list'})),
    path('<int:pk>/', ResumeView.as_view()),
]
