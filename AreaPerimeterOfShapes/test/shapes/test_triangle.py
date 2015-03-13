'''
Created on Mar 13, 2015

@author: deray
'''
import unittest
from shapes import Triangle, calculateTriangleArea

class TriangleTest(unittest.TestCase):

    def setUp(self):
        self._sideA = 5
        self._sideB = 10
        self._sideC = 15
        self.triangle = Triangle(self._sideA, self._sideB, self._sideC)


    def tearDown(self):
        pass


    def testValuesOfAllSides(self):
        self.assertEqual(self._sideA, self.triangle._sideA)
        
    def testPerimeter(self):
        actualPerimeter = self._sideA + self._sideB + self._sideC
        self.assertEqual(actualPerimeter, self.triangle.perimeter())
        
    def testArea(self):
        actualArea = calculateTriangleArea(self._sideA, self._sideB, self._sideC)
        self.assertEqual(actualArea, self.triangle.area())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
