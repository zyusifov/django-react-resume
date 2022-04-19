from .models import User
import hashlib
from rest_framework.exceptions import AuthenticationFailed


def get_user_data(request_data) -> User:
    email = request_data['email']
    password = request_data['password']

    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        'salt'.encode('utf-8'),
        100000
    )
    user = User.objects.filter(email=email).first()
    if user:
        if password_hash.hex() == user.password:
            return user
        else:
            raise AuthenticationFailed(code=403, detail='Email or password id invalid')
    else:
        raise AuthenticationFailed(code=403, detail='User not found')


def register_user(request_data):
    email = request_data['email']
    password = request_data['password']
    password2 = request_data['password2']

    if password == password2:
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            'salt'.encode('utf-8'),
            100000
        )
        user, is_created = User.objects.get_or_create(email=email, defaults={'email': email, 'password': password_hash})
        if is_created:
            return user
        else:
            raise AuthenticationFailed(detail='User already registered')
    else:
        raise AuthenticationFailed(detail='Passwords not equal')

