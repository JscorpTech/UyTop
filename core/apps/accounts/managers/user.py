from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, tg_id, first_name, **extra_fields):
        if not tg_id:
            raise ValueError(_("Telegram ID majburiy."))
        if not first_name:
            raise ValueError(_("Ism majburiy."))

        user = self.model(tg_id=tg_id, first_name=first_name, **extra_fields)
        user.set_unusable_password()  
        user.save(using=self._db)
        return user

    def create_superuser(self, tg_id, first_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser uchun is_staff=True bo‘lishi shart.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser uchun is_superuser=True bo‘lishi shart.")

        return self.create_user(tg_id=tg_id, first_name=first_name, **extra_fields)
