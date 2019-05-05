"""
Elliot Greenlee

04/07/2018

scraper.py
"""

import logging
import time

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException


def get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        response = requests.get(url, stream=True)
        if is_good_response(response):
            return response.content
        else:
            return None

    except RequestException as err:
        print(err)
        
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def scrape_recipe(recipe):
    url = "https://www.blueapron.com" + recipe
    print(url)
    html = get_html(url)
    
    title = get_title(html)
    description = get_description(html)
    ingredients = get_ingredients(html)
    time = get_time(html)
    servings = get_servings(html)
    calories = get_calories(html)
    instruction_titles, instruction_steps = get_instructions(html)
    
    recipe_file = open("../data" + recipe + ".txt", "w+")
    recipe_file.write(title + "\n")
    recipe_file.write(description + "\n")
    for ingredient in ingredients:
        recipe_file.write(ingredient[0] + "__" + ingredient[1] + "__" + ingredient[2] + "\n")
    recipe_file.write(time + "\n")
    recipe_file.write(servings + "\n")
    recipe_file.write(calories + "\n")
    for (instruction_title, instruction_step) in zip(instruction_titles, instruction_steps):
        recipe_file.write(instruction_title + "\n")
        recipe_file.write(instruction_step + "\n")
    
    
def get_html(url):
    raw_html = get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    return html


def get_title(html):
    title_object = html.find_all('h1', class_="ba-recipe-title__main")[0]
    sub_title_object = html.find_all('h2', class_="ba-recipe-title__sub mt-10")[0]
    return title_object.text.strip() + sub_title_object.text.strip()


def get_description(html):
    description_object = html.find_all('div', class_="recipe-main__description")[0]
    return description_object.text.strip()


def get_ingredients(html):
    ingredients_list = []
    ingredients_object = html.find_all('ul', class_="ba-info-list ba-info-list--stacked col-md-4")[0]
    for list_object in ingredients_object.find_all('li', class_="ba-info-list__item"):
    
        ingredient_object = list_object.find_all('a', class_="js-IngModalLink")
        if not ingredient_object:
            ingredient_object = list_object.find_all('div', class_="non-story")
        if not ingredient_object:
            print("help")
    
        ingredient_parsed = ingredient_object[0].text.splitlines()
        ingredient_magnitude = ingredient_parsed[2]
        ingredient_unit = ingredient_parsed[3]
        ingredient_name = ingredient_parsed[5]
        ingredients_list.append((ingredient_magnitude, ingredient_unit, ingredient_name))
        
    return ingredients_list


def get_time(html):
    spans = []
    recipe_main_list = html.find_all('div', class_="recipe-main-list")[0]
    for list_item in recipe_main_list.find_all('div', class_="ba-info-list__item-value"):
        for span in list_item.find_all('span'):
            spans.append(span)
    
    time_object = spans[0]
    return time_object.text.strip()
    
    
def get_servings(html):
    spans = []
    recipe_main_list = html.find_all('div', class_="recipe-main-list")[0]
    for list_item in recipe_main_list.find_all('div', class_="ba-info-list__item-value"):
        for span in list_item.find_all('span'):
            spans.append(span)
    
    servings_object = spans[2]
    return servings_object.text.strip()


def get_calories(html):
    spans = []
    recipe_main_list = html.find_all('div', class_="recipe-main-list")[0]
    for list_item in recipe_main_list.find_all('div', class_="ba-info-list__item-value"):
        for span in list_item.find_all('span'):
            spans.append(span)
    
    calorie_object = spans[5]
    return calorie_object.text.strip()


def get_instructions(html):
    instructions_titles = []
    instructions_steps = []
    instructions_html = html.find_all('section', class_="section-recipe recipe-instructions p-15")[0]
    instruction_step_htmls = instructions_html.find_all('div', class_="col-md-6 col-xs-12")
    
    for instruction_step_html in instruction_step_htmls:
        instruction_step_title_html = instruction_step_html.find_all('span', class_="step-title")[0]
        instruction_step_text_html = instruction_step_html.find_all('div', class_="step-txt")[0]
        
        instructions_titles.append(instruction_step_title_html.text.strip())
        instructions_steps.append(instruction_step_text_html.text.strip())
        
    return instructions_titles, instructions_steps


def main():
    recipe_names_file = open("../data/recipe_names_and_links.txt", 'r')

    recipes = []
    line_type = 0
    for line in recipe_names_file:
        if line_type == 0:
            recipes.append(line.strip())
        elif line_type == 1:
            image = line
        elif line_type == 2:
            title = line
        elif line_type == 3:
            subtitle = line
        elif line_type == 4:
            _ = line
        
        line_type += 1
        line_type = line_type % 5
    
    for recipe in recipes:
        print(recipe)
        scrape_recipe(recipe)
        time.sleep(5)
    

if __name__ == "__main__":
    main()
