from django import forms
from django.forms import widgets
from .models import Strength

STRENGTH_CHOICES = [
    (st.pump_turns, st.strength_name) 
    for st in Strength.objects.all() if st.strength_name != "Mixer"
    ]
class StrengthForm(forms.Form):
    strength = forms.CharField(label="How Strong??",
    widget=forms.Select(choices=STRENGTH_CHOICES))
