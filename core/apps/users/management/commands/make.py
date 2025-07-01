import hmac
import hashlib
import json
from urllib.parse import urlencode

from django.conf import settings

user = {
    "id": 434,
    "first_name": "Ali",
    "last_name": "Valiyev",
    "photo_url": "https://example.com/photo.jpg"
}

auth_date = 1719834843  

data = {
    "auth_date": str(auth_date),
    "user": json.dumps(user)  
}

check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))

secret_key = hashlib.sha256(settings.TELEGRAM_BOT_TOKEN.encode()).digest()

signature = hmac.new(secret_key, check_string.encode(), hashlib.sha256).hexdigest()

initdata = urlencode(data)

print("🔐 initdata:", f"{initdata}&hash={signature}")
print("🔑 hash (signature):", signature)
