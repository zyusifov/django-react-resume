from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import *
from .auth.base_auth import *


@api_view(["POST"])
def login(request):
    """ Подтверждение авторизации пользователя
    """
    user_data = get_user_data(request.data)
    token = create_token(user_data.id)
    return Response(token)


@api_view(["POST"])
def register(request):
    """ Подтверждение авторизации пользователя
    """
    user_data = register_user(request.data)
    token = create_token(user_data.id)
    return Response(token)
