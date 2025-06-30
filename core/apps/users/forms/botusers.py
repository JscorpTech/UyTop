from django import forms

from core.apps.users.models import BotusersModel


class BotusersForm(forms.ModelForm):

    class Meta:
        model = BotusersModel
        fields = "__all__"
