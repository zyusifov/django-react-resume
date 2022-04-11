from rest_framework import generics
from .serializer import *
from .models import *


class ResumeView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ResumeListView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ResumeCreatView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()