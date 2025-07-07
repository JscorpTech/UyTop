

def captio_text(listing, map_url):
    if listing.dealtype == 'sale':
        dealtype = "Sotiladi"
    else:
        dealtype = "Ijaraga beriladi"

    # Ta'mir turi tarjimasi
    if listing.repair_type == 'author':
        repair_type = 'Mualliflik loyihasi'
    elif listing.repair_type == 'euro':
        repair_type = 'Evrotamir'
    elif listing.repair_type == "medium":
        repair_type = 'O‘rtacha'
    elif listing.repair_type == "needs_repair":
        repair_type = 'Ta’mir talab'
    elif listing.repair_type == "black_finish":
        repair_type = 'Qora suvoq'
    else:
        repair_type = 'Noma’lum'

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
🗺 <a href="{map_url}">📍 Xaritada ko‘rish</a>

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
