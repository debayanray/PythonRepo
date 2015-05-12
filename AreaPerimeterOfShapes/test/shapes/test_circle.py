'''
Created on May 12, 2015

@author: rayd
'''
import unittest
from shapes.circle import Circle


class CircleTest(unittest.TestCase):


    def setUp(self):
        self._radius = 7
        self._circle = Circle(self._radius)


    def tearDown(self):
        pass


    def testRadiusOfCircle(self):
        self.assertEqual(self._radius, self._circle._radius)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()