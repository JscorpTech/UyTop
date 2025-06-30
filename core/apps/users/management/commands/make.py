from urllib.parse import urlencode
import hmac, hashlib, json
from django.conf import settings    

user = {
    "id": 434,
    "first_name": "Ali",
    "last_name": "Valiyev",
    "photo_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FImage&psig=AOvVaw2t8BGGtilHcGCoWv1hqUBv&ust=1751376211181000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCLCOxfmemY4DFQAAAAAdAAAAABAE"
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
