import telebot
import requests

from telebot import types
from django.conf import settings
from core.apps.api.models import ListingimageModel
from .texts import captio_text, ADMIN_CONFIRM, CHECK_ADMIN
from .buttons import listing_admin, chec_admin

import os



bot = telebot.TeleBot(token=settings.TELEGRAM_BOT_TOKEN)

from io import BytesIO
import os
import requests



def send_telegram(listing):
    map_url = f"https://yandex.com/maps/?ll={listing.longitude},{listing.latitude}&z=18"
    listing_url = f'https://uytop.felixits.uz/admin/api/listingmodel/{listing.id}/change/'
    images = ListingimageModel.objects.filter(listing=listing)

    media_group = []

    for img in images:
        img_bytes = BytesIO()
        try:
            # Local fayl borligini tekshirish
            if os.path.exists(img.image.path):
                with open(img.image.path, "rb") as f:
                    img_bytes.write(f.read())
                print(f"✅ Lokal rasm yuklandi: {img.image.path}")
            else:
                # Localda topilmasa URL dan yuklab olish
                img_url = f"{settings.BASE_URL}{img.image.url}"
                response = requests.get(img_url)
                if response.status_code == 200:
                    img_bytes.write(response.content)
                    print(f"✅ URL orqali rasm yuklandi: {img_url}")
                else:
                    print(f"❌ Rasm URL topilmadi yoki 404: {img_url}")
                    continue  # Bu rasmni o'tkazib yuboramiz

            img_bytes.name = os.path.basename(img.image.name)
            img_bytes.seek(0)  # Faylni boshiga qaytarish kerak
            media_group.append(types.InputMediaPhoto(media=img_bytes))

        except Exception as e:
            print(f"⚠️ Rasmni yuborishda xatolik: {e}")

    if media_group:
        try:
            bot.send_media_group(chat_id=settings.ADMIN, media=media_group)
        except Exception as e:
            print("❌ Rasmlar yuborishda xatolik:", e)
    else:
        print("⚠️ Hech qanday rasm topilmadi")

    try:
        caption_text = captio_text(listing, map_url)
        bot.send_message(
            chat_id=settings.ADMIN,
            text=caption_text,
            parse_mode="HTML"
        )
    except Exception as e:
        print("❌ Caption yuborishda xatolik:", e)

    try:
        bot.send_message(
            chat_id=settings.ADMIN,
            text=ADMIN_CONFIRM.format(listing.id),
            parse_mode="HTML",
            reply_markup=listing_admin(
                listing_id=listing.id,
                user_id=listing.user.tg_id,
                listing_url=listing_url
            )
        )
    except Exception as e:
        print("❌ Tugmalarni yuborishda xatolik:", e)




def send_check(check):
    if not check.image:
        print("⚠️ Xatolik: check.image mavjud emas")
        return

    image_path = check.image.path  
    if not os.path.exists(image_path):
        print("❌ Fayl topilmadi:", image_path)
        return

    caption = CHECK_ADMIN.format(
        lesson_id=check.listing.id,
        first_name=check.listing.user.first_name
    )


    admin_id = settings.ADMIN
    listing_id = check.listing.id
    user_id = check.listing.user.tg_id

    try:
        with open(image_path, 'rb') as photo:
            bot.send_photo(
                chat_id=admin_id,
                photo=photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=chec_admin(listing_id, user_id),
            )
    except Exception as e:
        print("Telegramga yuborishda xatolik:", e)

