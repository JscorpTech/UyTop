from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton





def listing_admin(listing_id, user_id, listing_url):
    listing_button = InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"listing_check_{listing_id}_{user_id}")
            ],
            [
                InlineKeyboardButton(text="✏️ Tahrirlash", url=listing_url)
            ],
            [
                InlineKeyboardButton(text="❌ Rad etish", callback_data=f"listing_cancel_{listing_id}_{user_id}")
            ],
        ]
    )
    
    return listing_button



    
def chec_admin(listing_id, user_id):
    chec_button = InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"check_{listing_id}_{user_id}")
            ]
        ]
    )
    return chec_button

    