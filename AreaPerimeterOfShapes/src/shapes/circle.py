'''
Created on Mar 12, 2015

@author: deray
'''
from math import pi
from shapes.shape import Shape

class Circle(Shape):
    '''
    Circle class
    '''
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return pi * self._radius * self._radius


    def perimeter(self):
        return 2 * pi * self._radius

        
    