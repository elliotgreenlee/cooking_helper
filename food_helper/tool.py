"""
Elliot Greenlee

11/23/2018

tool.py
"""

from food_helper.tools import generate_id


class Tool:
    def __init__(self, name, description):
        self.id = generate_id(name)
        self.name = name
        self.description = description

