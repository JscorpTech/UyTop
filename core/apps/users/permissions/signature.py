import hmac, hashlib, json
from urllib.parse import parse_qsl
from django.conf import settings
from core.apps.users.models import BotusersModel




def parse_auth_botuser(init_data: str, signature: str, request=None):
    try:
        data = dict(parse_qsl(init_data))
        hash_from_telegram = data.pop("hash", None)
        if not hash_from_telegram:
            return None

        check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
        secret_key = hashlib.sha256(settings.TELEGRAM_BOT_TOKEN.encode()).digest()
        calculated_hash = hmac.new(secret_key, check_string.encode(), hashlib.sha256).hexdigest()

        if not hmac.compare_digest(calculated_hash, hash_from_telegram):
            return None

        user_raw = data.get("user")
        if not user_raw:
            return None

        user_data = json.loads(user_raw)
        tg_id = user_data.get("id")
        first_name = user_data.get("first_name", "user")
        last_name = user_data.get("last_name", "")
        photo_url = user_data.get("photo_url", "")

        bot_user, created = BotusersModel.objects.get_or_create(
            tg_id=tg_id,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "photo_url": photo_url
            }
        )

        if not created:
            updated = False
            if bot_user.first_name != first_name:
                bot_user.first_name = first_name
                updated = True
            if bot_user.last_name != last_name:
                bot_user.last_name = last_name
                updated = True
            if bot_user.photo_url != photo_url:
                bot_user.photo_url = photo_url
                updated = True
            if updated:
                bot_user.save()

        if request:
            request.bot_user = bot_user

        return bot_user

    except Exception as e:
        print("Xatolik:", e)
        return None
