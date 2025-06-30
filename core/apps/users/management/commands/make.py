from urllib.parse import urlencode
import hmac, hashlib, json
from django.conf import settings    

user = {
    "id": 4,
    "name": "HUsanjon",
}
auth_date = 1719834843

data = {
    "user": json.dumps(user, separators=(",", ":")),
    "auth_date": str(auth_date),
}

initdata = urlencode(data)

secret_key = settings.SECRET_KEY  
signature = hmac.new(secret_key.encode(), initdata.encode(), hashlib.sha256).hexdigest()

print("initdata:", initdata)
print("signature:", signature)
