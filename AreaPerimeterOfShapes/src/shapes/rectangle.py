'''
Created on Mar 12, 2015

@author: deray
'''
from shapes.shape import Shape

class Rectangle(Shape):
    '''
    Rectangle class
    '''

    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    def area(self):
        return self._length * self._breadth


    def perimeter(self):
        return 2 * (self._length + self._breadth)


    
        