"""
Elliot Greenlee

11/22/2018

Meal.py
"""

from food_helper.tools import generate_id
from collections import set


class Meal:
    def __init__(self, name, cook_time, servings, description, wine_pairing, instructions,
                 ease=None, taste=None):
        
        self.id = generate_id(name)  # meal identification string
        self.name = name  # name of the meal
        self.description = description  # overall meal description
        
        self.cook_time = cook_time  # total meal cook time
        self.servings = servings  # how many total people will this feed
        self.wine_pairing = wine_pairing  # the type of wine that fits this meal
        
        self.cuisines = set()  # style of cooking
        self.seasons = set()  # season of the year

        self.instructions = instructions  # pipelined instructions to cook this set of recipes

        self.ease = self.determine_ease(ease=ease)  # how easy is it to cook
        self.taste = self.determine_taste(taste=taste)  # how good does it taste
        
        self.recipes = []  # component recipe ids
        
        self.nutrition_card = None
        
    def add_cuisine(self, cuisine):
        self.cuisines.add(cuisine)
        
    def add_seasons(self, season):
        self.seasons.add(season)

    @staticmethod
    def determine_ease(ease=None):
        
        # TODO: use ml and scraping to determine ease if not set
        return ease
    
    @staticmethod
    def determine_taste(taste=None):
        
        # TODO: use ml and scraping to determine taste if not set
        return taste
        
    def add_recipe(self, recipe_id):
        self.recipes.append(recipe_id)
        
    def set_nutrition_card(self, nutrition_card):
        self.nutrition_card = nutrition_card
        
    def get_tools(self):
        tools = set()
        
        for recipe_id in self.recipes:
            recipe = get_recipe(recipe_id)
            
            tools.update(recipe.tools)
            
        return tools
    
    def get_ingredients(self):
        ingredients = {}
        
        for recipe_id in self.recipes:
            recipe = get_recipe(recipe_id)
            
            ingredients.update(recipe.ingredients)  # TODO add the amounts together if there is a repeat
            
        return ingredients
    





