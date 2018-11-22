"""
Elliot Greenlee

11/22/2018

recipe.py
"""

from food_helper.tools import generate_id


class Recipe:
    def __init__(self, name, description, cook_time, servings, food_type, ease, taste):
        self.id = generate_id(name)  # recipe identification string
        self.name = name  # name of the recipe
        self.description = description  # overall recipe description

        self.cook_time = cook_time  # total meal cook time
        self.servings = servings  # how many total people will this feed
        
        self.food_type = food_type  # type of food
        
        self.cuisines = set()  # style of cooking
        self.seasons = set()  # season of the year
        
        # TODO: figure out how to keep track of units
        self.ingredients = {}  # a dictionary of key:ingredient_id and value:amounts
        self.tools = []  # a list of needed tools
        
        self.ease = ease  # how easy is it to cook
        self.taste = taste  # how good does it taste
        
        
        







