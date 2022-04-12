from rest_framework import generics, viewsets
from .serializer import *
from .models import *


class ResumeView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ResumeListView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ResumeCreateView(generics.CreateAPIView):
    serializer_class = UserResumeSerializer
    queryset = Resume.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserResumeView(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    
    def get_queryset(self):
        return Resume.objects.filter(user_id=self.kwargs.get('pk'))