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
    

class NutritionCard:
    def __init__(self, calories_amount, calories_percent_daily_serving,
                 total_fat_amount, total_fat_percent_daily_serving,
                 trans_fat_amount, trans_fat_percent_daily_serving,
                 cholesterol_amount, cholesterol_percent_daily_serving,
                 sodium_amount, sodium_percent_daily_serving,
                 carbs_amount, carbs_percent_daily_serving,
                 fiber_amount, fiber_percent_daily_serving,
                 sugars_amount, sugars_percent_daily_serving,
                 protein_amount, protein_percent_daily_serving,
                 vitamin_a=0, vitamin_c=0, calcium=0, iron=0):
        
        self.calories = Nutrient(calories_amount, calories_percent_daily_serving)  # calories per serving
        self.total_fat = Nutrient(total_fat_amount, total_fat_percent_daily_serving)  # total fat per serving
        self.trans_fat = Nutrient(trans_fat_amount, trans_fat_percent_daily_serving)  # trans-fatty acid per serving
        self.cholesterol = Nutrient(cholesterol_amount, cholesterol_percent_daily_serving)  # cholesterol per serving
        self.sodium = Nutrient(sodium_amount, sodium_percent_daily_serving)  # salt per serving
        self.carbs = Nutrient(carbs_amount, carbs_percent_daily_serving)  # carbohydrates per serving
        self.fiber = Nutrient(fiber_amount, fiber_percent_daily_serving)  # fiber per serving
        self.sugars = Nutrient(sugars_amount, sugars_percent_daily_serving)  # sugar per serving
        self.protein = Nutrient(protein_amount, protein_percent_daily_serving)  # protein per serving
        
        self.vitamin_a = vitamin_a  # vitamin A per serving
        self.vitamin_c = vitamin_c  # vitamin C per serving
        self.calcium = calcium  # calcium per serving
        self.iron = iron  # iron per serving
        
        
class Nutrient:
    def __init__(self, amount, percent_daily_serving):
        self.amount = amount
        self.percent_daily_serving = percent_daily_serving
        
        
class Vitamin:
    def __init__(self, percent_daily_serving):
        self.percent_daily_serving = percent_daily_serving

        
        





