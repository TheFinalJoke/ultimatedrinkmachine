from typing import Reversible
from django.contrib import admin

from .models import (
    Recipe, 
    PumpToALiquid, Strength
)

models = [Recipe, PumpToALiquid, Strength]
admin.site.register(models)