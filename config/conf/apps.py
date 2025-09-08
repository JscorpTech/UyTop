from config.env import env

APPS = [
    "channels",
    "cacheops",
    "rosetta",
    "django_ckeditor_5",
    "parler",
    "drf_spectacular",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_redis",
    "rest_framework_simplejwt",
    "django_core",
    "core.apps.accounts.apps.AccountsConfig",
    "core.apps.api",
    "core.apps.users",
    
]

if env.bool("SILK_ENEBLED", False):
    APPS += [
        "silk",
    ]
