from django import forms
from django.forms import fields

from Hotels.models import Hotel




class HotelForm(forms.ModelForm):
    class Meta:
        model=Hotel
        fields="__all__"

