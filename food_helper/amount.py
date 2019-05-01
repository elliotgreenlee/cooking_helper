"""
Elliot Greenlee

11/23/2018

amount.py
"""

from pint import UnitRegistry


class Amount:
    
    def __init__(self, magnitude, unit):
        ureg = UnitRegistry()
        # todo: add a try so if it fails to parse expression (like "head of cabbage" maybe?)
        self.quantity = magnitude * ureg.parse_expression(unit)
