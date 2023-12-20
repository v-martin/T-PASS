from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def get_or_create_token(user: User) -> None:
    return Token.objects.get_or_create(user=user)


def create_user(data: dict) -> User:
    return User.objects.create_user(**data)
