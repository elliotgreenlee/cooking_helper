"""
Elliot Greenlee

11/23/2018

ingredient.py
"""

from food_helper.tools import generate_id


class Ingredient:
    def __init__(self, name, description, amount, units):
        self.id = generate_id(name)  # ingredient identification string
        self.name = name  # name of the ingredient
        self.description = description  # description of the ingredient
        self.amount = amount  # amount of the ingredient in units
        self.units = units  # unit for the amount of the ingredient
        
        self.seasons = set()  # season of the year
        
        
    







