from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Foydalanuvchilar"),
        "separator": True,  
        "items": [
            {
                "title": _("Users"),
                "icon": "person",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "title": _("Kategorya va Tumanlar "),
        "separator": True,  
        "items": [
            {
                "title": _("Kategoryalar"),
                "icon": "category",
                "link": reverse_lazy("admin:api_categorymodel_changelist"),
            },
            {
                "title": _("Tuman"),
                "icon": "location_city",
                "link": reverse_lazy("admin:api_districtmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Uy bo'yicha bo'limlar"),
        "separator": True,  
        "items": [
            {
                "title": _("Uy elonlari"),
                "icon": "home_work",
                "link": reverse_lazy("admin:api_listingmodel_changelist"),
            },
            {
                "title": _("Qurilish materiallari"),
                "icon": "construction",
                "link": reverse_lazy("admin:api_buildingmaterialmodel_changelist"),
            },
            # {
            #     "title": _("E'lon osti turlari"),
            #     "icon": "layers",
            #     "link": reverse_lazy("admin:api_propertysubtypemodel_changelist"),
            # },
            {
                "title": _("Qulayliklar"),
                "icon": "weekend",
                "link": reverse_lazy("admin:api_amenitymodel_changelist"),
            },
        ],
    },
]
