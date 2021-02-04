from lib.protocol import ALCOHOL_TO_PUMP
from django import forms
import pdb
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
    widget=forms.Select(choices=STRENGTH_CHOICES, attrs={'class': 'form-select form-select-lg mb-3', 'style': 'font-size: xx-large'}))


class AddDrinkForm(forms.Form):
    ALL_LIQUID_CHOICES = [
    (liq.pump_num, liq.liquid, liq.liquid_type)
    for liq in PumpToALiquid.objects.all()
    ]
    ALCOHOL_CHOCIES = [(liq[0], liq[1]) for liq in ALL_LIQUID_CHOICES if liq[2] == "Alcohol"]
    MIXER_CHOCIES = [(liq[0], liq[1]) for liq in ALL_LIQUID_CHOICES if liq[2] == "Mixer"]
    name = forms.CharField(label="Name For Recipe:", max_length=50)
    Alcohol = forms.CharField(label="Alcohol",
    widget=forms.Select(choices=ALCOHOL_CHOCIES, attrs={'class': 'form-control'}))
    Mixer = forms.CharField(label="Mixer",
    widget=forms.Select(choices=MIXER_CHOCIES, attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(AddDrinkForm, self).__init__(*args, **kwargs)
        self.ALL_LIQUID_CHOICES = [(liq.pump_num, liq.liquid, liq.liquid_type) 
                                    for liq in PumpToALiquid.objects.all()]
        self.fields['Alcohol'].widget.choices = [(liq[0], liq[1]) for liq in self.ALL_LIQUID_CHOICES if liq[2] == "Alcohol"]
        self.fields['Mixer'].widget.choices = [(liq[0], liq[1]) for liq in self.ALL_LIQUID_CHOICES if liq[2] == "Mixer"]

class DeleteDrinkForm(forms.Form):
    RECIPE_CHOICES = [(rec.id, rec.name) for rec in Recipe.objects.all()]
    Recipes = forms.CharField(label="Choose a Recipe",
    widget=forms.Select(choices=RECIPE_CHOICES, attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super(DeleteDrinkForm, self).__init__(*args, **kwargs)
        self.fields['Recipes'].widget.choices = [(rec.id, rec.name) for rec in Recipe.objects.all()]