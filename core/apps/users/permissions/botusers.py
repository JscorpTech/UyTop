from rest_framework import permissions

from nacl.signing import VerifyKey
from nacl.exceptions import  BadSignatureError
from config.env import env
from core.apps.users.models import BotusersModel

import base64
import json


class BotusersPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True
