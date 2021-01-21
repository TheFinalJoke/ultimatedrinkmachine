from lib.protocol import ALCOHOL_TO_PUMP
from django import forms
from django.forms import widgets
from .models import (
    Strength,
    PumpToALiquid,
    Recipe
)

class StrengthForm(forms.Form):
    STRENGTH_CHOICES = [
    (st.pump_turns, st.strength_name) 
    for st in Strength.objects.all() if st.strength_name != "Mixer"
    ]
    strength = forms.CharField(label="How Strong??",
    widget=forms.Select(choices=STRENGTH_CHOICES))


class AddDrinkForm(forms.Form):
    ALL_LIQUID_CHOICES = [
    (liq.pump_num, liq.liquid, liq.liquid_type)
    for liq in PumpToALiquid.objects.all()
    ]
    ALCOHOL_CHOCIES = [(liq[0], liq[1]) for liq in ALL_LIQUID_CHOICES if liq[2] == "Alcohol"]
    MIXER_CHOCIES = [(liq[0], liq[1]) for liq in ALL_LIQUID_CHOICES if liq[2] == "Mixer"]
    name = forms.CharField(label="Name For Recipe:", max_length=50)
    Alcohol = forms.CharField(label="Alcohol",
    widget=forms.Select(choices=ALCOHOL_CHOCIES))
    Mixer = forms.CharField(label="Mixer",
    widget=forms.Select(choices=MIXER_CHOCIES))

class DeleteDrinkForm(forms.Form):
    RECIPE_CHOICES = [(rec.id, rec.name) for rec in Recipe.objects.all()]
    Recipes = forms.CharField(label="Choose a Recipe",
    widget=forms.Select(choices=RECIPE_CHOICES))