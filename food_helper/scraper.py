"""
Elliot Greenlee

04/07/2018

scraper.py
"""

import logging

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


url = "https://www.blueapron.com/recipes/curry-chicken-pitas-with-cucumber-yogurt-sweet-chili-slaw"
raw_html = get(url)
html = BeautifulSoup(raw_html, 'html.parser')

print(html)

# title
title_object = html.find_all('h1', class_="ba-recipe-title__main")[0]
print(title_object.text)

sub_title_object = html.find_all('h2', class_="ba-recipe-title__sub mt-10")[0]
print(sub_title_object.text)

# description
description_object = html.find_all('div', class_="recipe-main__description")[0]
print(description_object.text)


# time, servings, calories
spans = []
recipe_main_list = html.find_all('div', class_="recipe-main-list")[0]
for list_item in recipe_main_list.find_all('div', class_="ba-info-list__item-value"):
    for span in list_item.find_all('span'):
        spans.append(span)
        
time_object = spans[0]
print(time_object.text)
servings_object = spans[2]
print(servings_object.text)
calorie_object = spans[5]
print(calorie_object.text)

    

