"""
Elliot Greenlee

11/23/2018

units.py
"""

from pint import UnitRegistry


class Amount:
    
    def __init__(self, magnitude, unit):
        ureg = UnitRegistry()
        self.quantity = magnitude * ureg.parse_expression(unit)
