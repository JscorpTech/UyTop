import telebot
import requests

from telebot import types
from django.conf import settings
from core.apps.api.models import ListingimageModel
from .texts import captio_text, ADMIN_CONFIRM, CHECK_ADMIN
from .buttons import listing_admin, chec_admin

import os



bot = telebot.TeleBot(token=settings.TELEGRAM_BOT_TOKEN)


def send_telegram(listing):
    map_url = f"https://yandex.com/maps/?ll={listing.longitude},{listing.latitude}&z=18"
    listing_url=f'http://127.0.0.1:8042/admin/api/listingmodel/{listing.id}/change/'
    images = ListingimageModel.objects.filter(listing=listing)
    

    media_group = []
    for i, img in enumerate(images):
        img_url = f"{settings.BASE_URL}{img.image.url}"
        try:
            response = requests.get(img_url)
            if response.status_code != 200:
                continue
            if i == 0:
                media_group.append(
                    types.InputMediaPhoto(
                        media=img_url,
                        caption=captio_text(listing, map_url, listing_url),
                        parse_mode="HTML"
                    )
                )
            else:
                media_group.append(types.InputMediaPhoto(media=img_url))
        except:
            continue


    if media_group:
        bot.send_media_group(settings.ADMIN, media=media_group)
    else:
        bot.send_message(settings.ADMIN, captio_text(listing, map_url), parse_mode="HTML")

    listing_id = listing.id
    user_id = listing.user.tg_id
    

    bot.send_message(
        chat_id=settings.ADMIN,
        text=ADMIN_CONFIRM.format(listing.id),
        parse_mode="HTML",
        reply_markup=listing_admin(listing_id, user_id, listing_url)
    )



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

