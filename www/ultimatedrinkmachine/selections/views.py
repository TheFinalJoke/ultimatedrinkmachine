from django import template
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import generic
from .models import Recipe, PumpToALiquid, Strength
from .forms import (
    DeleteDrinkForm, StrengthForm,
    AddDrinkForm
)
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

def add_drink(request):
    drinkform = AddDrinkForm()
    return render(request, 'selections/add_drink.html', {"drinkform": drinkform})

def delete_recipe(request):
    deleteform = DeleteDrinkForm()
    return render(request, 'selections/deleterecipe.html', {"deleteform": deleteform})
def post_adddrink(request):
    if request.method == "POST":
        form = AddDrinkForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            alcohol = form.cleaned_data['Alcohol']
            mixer = form.cleaned_data['Mixer']
            alcohol_obj = PumpToALiquid.objects.filter(pump_num=alcohol)[0]
            mixer_obj = PumpToALiquid.objects.filter(pump_num=mixer)[0]
            Recipe_obj = Recipe(
                name=name, 
                alcohol=alcohol_obj, 
                mixer=mixer_obj)
            Recipe_obj.save()
    return redirect('/selections/')

def post_delete(request):
    if request.method == "POST":
        form = DeleteDrinkForm(request.POST)
        if form.is_valid():
            rec = form.cleaned_data['Recipes']
            recipe_obj = Recipe.objects.filter(pk=rec)[0]
            recipe_obj.delete()
    return redirect('/selections/')
            