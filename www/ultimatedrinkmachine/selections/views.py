from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.views import generic
from .models import Recipe, PumpToALiquid

class IndexView(generic.ListView):
    template_name = 'selections/index.html'
    context_object_name = 'recipes'
    def get_queryset(self):
        return Recipe.objects.all()

class SelectedView(generic.DetailView):
    model = Recipe
    template_name = "selections/selected.html"