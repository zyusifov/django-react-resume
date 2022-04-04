from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, ResumeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models.user import User
from .models.resume import Resume
from rest_framework import generics, exceptions
from rest_framework.views import APIView


# Auth

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# User data

class MeDataView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({"id": request.user.id, "user": request.user.email})


class UserDataView(generics.GenericAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    lookup_url_kwarg = 'user_id'

    def get_object(self):
        try:
            resume = Resume.objects.get(user_id=self.kwargs.get('user_id'))
        except:
            raise exceptions.NotFound
        return resume

    def get(self, request, user_id):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)