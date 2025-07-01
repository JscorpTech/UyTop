from rest_framework import permissions
from .signature import parse_auth_botuser



class BotusersPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        init_data = request.headers.get("initdata")
        signature = request.headers.get("token")


        print(init_data)
        print(signature)
        if not init_data or not signature:
            return False
        print(request)
        bot_user = parse_auth_botuser(init_data=init_data, signature=signature, request=request)
        if not bot_user:
            return False

        request.bot_user = bot_user
        return True
