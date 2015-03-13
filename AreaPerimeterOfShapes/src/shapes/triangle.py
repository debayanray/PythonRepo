'''
Created on Mar 13, 2015

@author: deray
'''
from shapes.shape import Shape
import math

class Triangle(Shape):
    '''
    Triangle class
    '''    
    def __init__(self, sideA, sideB, sideC):
        self._sideA = sideA
        self._sideB = sideB
        self._sideC = sideC

    def perimeter(self):
        if not hasattr(self, '_perimeter'):
            self._perimeter = self._sideA + self._sideB + self._sideC
            
        return self._perimeter
    
    def area(self):
        return calculateTriangleArea(self._sideA, self._sideB, self._sideC)
    

# based on Heron Formula (http://en.wikipedia.org/wiki/Heron's_formula)
def calculateTriangleArea(sideA, sideB, sideC):
    semiPerimeter = (sideA + sideB + sideC) / 2
    return math.sqrt(semiPerimeter * (semiPerimeter - sideA) * (semiPerimeter - sideB) * (semiPerimeter - sideC))
