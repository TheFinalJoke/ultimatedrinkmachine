from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class PumpToALiquid(models.Model):
    liquid = models.CharField(max_length=200)
    pump_num = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.liquid

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    alcohol = models.ForeignKey(
        PumpToALiquid, 
        on_delete=models.CASCADE,
        related_name="Alcohol"
    )
    mixer = models.ForeignKey(
        PumpToALiquid, 
        on_delete=models.CASCADE,
        related_name="Mixer"
        )
    def __str__(self) -> str:
        return self.name

class Strength(models.Model):

    strength_name = models.CharField(max_length=50)
    pump_turns = models.PositiveSmallIntegerField()
    def __str__(self) -> str:
        return self.strength_name