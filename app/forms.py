from django import forms

from app.models import *


class VillageForm(forms.ModelForm):
    class Meta:
        model=Village
        fields='__all__'