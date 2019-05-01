"""
Elliot Greenlee

11/23/2018

ingredient.py
"""

from food_helper.tools import generate_id
from food_helper import amount


class Ingredient:
    def __init__(self, name, description, magnitude, unit):
        self.id = generate_id(name)  # ingredient identification string
        self.name = name  # name of the ingredient
        self.description = description  # description of the ingredient
        self.amount = amount.Amount(magnitude, unit)  # amount of the ingredient in units
        
        self.seasons = set()  # season of the year
        
        
    







