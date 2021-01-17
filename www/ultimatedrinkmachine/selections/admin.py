from typing import Reversible
from django.contrib import admin

from .models import Recipe, PumpToALiquid

models = [Recipe, PumpToALiquid]
admin.site.register(models)