from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import User
from rest_framework import generics
from rest_framework. views import APIView

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# for testing
class Welcome(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):

        return Response({"key": "Hello !"})