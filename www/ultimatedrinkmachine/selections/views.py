from django import template
import pdb
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import generic
from .models import Recipe, PumpToALiquid, Strength
from .forms import StrengthForm
from lib.protocol import (
    DrinkClientSocket,
    DrinkProtocol,
    ALCOHOL_TO_PUMP
)

class IndexView(generic.ListView):
    template_name = 'selections/index.html'
    context_object_name = 'recipes'
    def get_queryset(self):
        return Recipe.objects.all()

def forms_selected(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)  
    form = StrengthForm()
    return render(request, 'selections/selected.html', {'form': form, 'recipe': recipe})

def package(request, recipe_id):
    if request.method == "POST":
        form = StrengthForm(request.POST)
        if form.is_valid():
            transform = DrinkProtocol()
            recipe = get_object_or_404(Recipe, id=recipe_id)
            strength = form.cleaned_data['strength']
            transformed_recipe = transform.transform(
                recipe.name, 
                recipe.alcohol.liquid,
                recipe.mixer.liquid,
                int(strength))
            drinksock = DrinkClientSocket()
            drinksock.connect()
            recv = drinksock.send_data(transformed_recipe)           
            return render(request, 'selections/post_dispense.html', {'recv': recv})

def post_dispense(request, recipe_id):
    return render(request, 'selections/post_dispense.html')
