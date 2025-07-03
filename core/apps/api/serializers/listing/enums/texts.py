
    


def captio_text(listing, map_url):
    
    if listing.dealtype == 'sale':
        dealtype = "Sotiladi"
    else:
        dealtype = "Ijaraga beriladi"
    
    
    if listing.repair_type == 'author':
        repair_type = 'Avtorlik loyihasi'
    elif listing.repair_type == 'euro':
        repair_type = 'Evrotamir'
    elif listing.repair_type == "medium":
        repair_type = 'O‘rta'
    elif listing.repair_type == "needs_repair":
        repair_type = 'Ta’mir talab'
    elif listing.repair_type == "black_finish":
        repair_type = 'Qora suvoq'
        
        
    
    caption = f"""🏠 <b>Yangi e'lon qo‘shildi!</b>\n
    📌 <b>Nomi:</b> {listing.name}
    💵 <b>Narxi:</b> {listing.price} {listing.currency} {"(Kelishiladi)" if listing.negotiable else ""}
    🏘 <b>Deal type:</b> {dealtype}
    🏢 <b>Property:</b> {listing.property} ({listing.property_subtype})
    🛏 <b>Xonalar:</b> {listing.room_count}
    📐 <b>Maydon:</b> {listing.apartment_area or listing.house_area or listing.land_area or "-"} m²
    🛠 <b>Ta'mirlash:</b> {repair_type}
    📞 <b>Telefon:</b> {listing.phone}
    📍 <b>Manzil:</b> {listing.address}
    🗺 <a href="{map_url}">📍 Xaritada ochish</a>\n
    📝 <b>Tavsif:</b> {listing.description if listing.description else "Yo‘q"}
    """
    
    return caption

ADMIN_CONFIRM = \
"""
e'loni tasdiqlashingiz bilan elon active bo'ladi
E'lon id: <code>{}</code>
"""

CHECK_ADMIN = \
"""
✅ To'lov tasdiqlandi!

🆔 E'lon ID: <code>{lesson_id}</code> 
👤 Foydalanuvchi: {first_name}

E'lon tizimda faol holatga o'tdi.
"""
