
def captio_text(listing, map_url):
    # Deal type
    dealtype = "Sotiladi" if listing.dealtype == 'sale' else "Ijaraga beriladi"

    # Ta'mir turi
    repair_type_map = {
        'author': 'Mualliflik loyihasi',
        'euro': 'Evrotamir',
        'medium': 'O‘rtacha',
        'needs_repair': 'Ta’mir talab',
        'black_finish': 'Qora suvoq'
    }
    repair_type = repair_type_map.get(listing.repair_type, 'Noma’lum')

    # Top listing kunlari (agar mavjud bo'lsa)
    toplisting_text = ""
    if getattr(listing, 'toplisting', None):
        toplisting_day = getattr(listing.toplisting, 'day', None)
        if toplisting_day:
            toplisting_text = f"\n⭐ <b>Top elon:</b> {toplisting_day} kun"

    caption = f"""🏠 <b>Yangi e’lon qo‘shildi!</b>
📌 <b>Nomi:</b> {listing.name}
💵 <b>Narxi:</b> {listing.price} {listing.currency} {"(Kelishiladi)" if listing.negotiable else ""}
📃 <b>Holati:</b> {dealtype}
🏢 <b>Turi:</b> {listing.property} ({listing.property_subtype})
🛏 <b>Xonalar soni:</b> {listing.room_count}
📐 <b>Maydon:</b> {listing.apartment_area or listing.house_area or listing.land_area or "-"} m²
🛠 <b>Ta’mir holati:</b> {repair_type}
📞 <b>Aloqa:</b> {listing.phone}
📍 <b>Manzil:</b> {listing.address}
🌐 <b>Tuman:</b> {listing.region}
🗺 <a href="{map_url}">📍 Xaritada ko‘rish</a>{toplisting_text}

📝 <b>Tavsif:</b> {listing.description if listing.description else "Mavjud emas"}
"""
    return caption


ADMIN_CONFIRM = \
"""
E'lonni tasdiqlaganingizdan so‘ng u faol holatga o‘tadi.

🆔 E'lon ID: <code>{}</code>
"""


CHECK_ADMIN = \
"""
✅ To‘lov tasdiqlandi!

🆔 E'lon ID: <code>{lesson_id}</code>  
👤 Foydalanuvchi: {first_name}

E'lon tizimda muvaffaqiyatli tarzda faol holatga o‘tkazildi.
"""
