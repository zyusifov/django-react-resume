from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .utils import Util
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
    """ Регистрация пользователя
    """
    user_data = register_user(request.data)
    token = create_token(user_data.id)
    domain = f"http://127.0.0.1:8000/auth/verify/?token={token['access_token']}" 
    Util.send_email(domain, user_data.email)
    return Response({"detail": "Confirm your email"})


@api_view(["GET"])
def verify_email(request):
    """ Подтверждение пользователя
    """
    if "token" in request.GET:
        token = request.GET['token']
        if verify_user(token):
            return Response({"detail": "Email verified"})
        else:
            return Response({"detail": "Email not verified"})
    else:
        return Response(AuthenticationFailed)
        