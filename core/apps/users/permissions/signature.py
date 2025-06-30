import hmac
import hashlib
import json
from urllib.parse import parse_qsl
from django.conf import settings
from core.apps.users.models import BotusersModel




def parse_auth_botuser(init_data: str, signature: str, request=None):
    secret_key = settings.SECRET_KEY.encode()
    computed_signature = hmac.new(secret_key, init_data.encode(), hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature, computed_signature):
        return None

    try:
        data = dict(parse_qsl(init_data))
        user_raw = data.get("user")

        if not user_raw:
            return None

        user_data = json.loads(user_raw)
        tg_id = user_data.get("id")
        name = user_data.get("name", "user")

        if not tg_id:
            return None

        bot_user, created = BotusersModel.objects.get_or_create(
            tg_id=tg_id,
            defaults={"name": name}
        )

        if not created and bot_user.name != name:
            bot_user.name = name
            bot_user.save()

        return bot_user

    except Exception as e:
        print("Xatolik:", e)
        return None
