import telebot
import requests

from telebot import types

from django.conf import settings
from core.apps.api.models import ListingimageModel
from .texts import captio_text, ADMIN_CONFIRM, CHECK_ADMIN


bot = telebot.TeleBot(token=settings.TELEGRAM_BOT_TOKEN)



def send_telegram(listing):
    chat_id = settings.ADMIN

    map_url = f"https://yandex.com/maps/?ll={listing.longitude},{listing.latitude}&z=18"


    images = ListingimageModel.objects.filter(listing=listing)
    if not images:
        bot.send_message(chat_id, captio_text(listing, map_url), parse_mode="HTML")
        return

    media_group = []
    for i, img in enumerate(images):
        img_url = f"{settings.BASE_URL}{img.image.url}"
        
        try:
            response = requests.get(img_url)
            if response.status_code != 200:
                continue 

            if i == 0:
                media_group.append(types.InputMediaPhoto(media=img_url, caption=captio_text(listing, map_url), parse_mode="HTML"))
            else:
                media_group.append(types.InputMediaPhoto(media=img_url))
        except:
            continue

    if media_group:
        bot.send_media_group(chat_id, media=media_group)
    else:
        bot.send_message(chat_id, captio_text(listing, map_url), parse_mode="HTML")



    
    bot.send_message(
        chat_id=settings.ADMIN,
        text=ADMIN_CONFIRM.format(listing.id),
        parse_mode="HTML"
    )


def send_check(check):
    image = check.image
    
    caption = CHECK_ADMIN.format(
        lesson_id=check.listing.id,
        first_name=check.listing.user.first_name
    )
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton(text="Tasdiqlash ✅", callback_data=f"check_{check.listing.id}_{check.listing.user.tg_id}"))

    bot.send_photo(
        chat_id=settings.ADMIN,
        photo=image,
        caption=caption,
        parse_mode="HTML",
        reply_markup=button,
    )

