'''
Created on Mar 12, 2015

@author: deray
'''
from abc import ABCMeta, abstractmethod

class Shape(object):
    '''
    Abstract class Shape
    '''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
        