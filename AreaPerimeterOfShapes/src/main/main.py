'''
Created on Mar 12, 2015

@author: deray
'''
from shapes import Circle
from shapes import Rectangle

if __name__ == '__main__':
    
    circle = Circle(5)
    print("Circle: Area is %.2f" % circle.area())
    print("Circle: Perimeter is %.2f" % circle.perimeter())
    
    rectangle = Rectangle(10, 5)
    print("Rectangle: Area is %.2f" % rectangle.area())
    print("Rectangle: Perimeter is %.2f" % rectangle.perimeter())

