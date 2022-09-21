# -*- coding: utf-8 -*-
"""
Updated sep 21, 2022
The primary goal of this file is to demonstrate a simple unittest implementation
@author: rao
@author: pranav
"""

import unittest

class TestTriangles(unittest.TestCase):


    def testInvalidTriangles(self):
        self.assertEqual(classify_triangle(1,3,5),'NotATriangle','1,3,5 is not a Triangle')
    def testInvalidTriangles2(self):
        self.assertEqual(classify_triangle(1,4,5),'NotATriangle','1,4,5 is not a Triangle')
    def testInvalidTriangles3(self):
        self.assertEqual(classify_triangle(1,0,1),'NotATriangle','1,0,1 is not a Triangle')

    def testRightTriangles(self):
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangles2(self):
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangles3(self):
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTriangles2(self):
        self.assertEqual(classify_triangle(3,3,3),'Equilateral','3,3,3 should be equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classify_triangle(5,5,1),'Isoceles','5,5,1 should be isoceles')
    def testIsocelesTriangles2(self):
        self.assertEqual(classify_triangle(5,1,5),'Isoceles','5,1,5 should be isoceles')
    def testIsocelesTriangles3(self):
        self.assertEqual(classify_triangle(1,5,5),'Isoceles','1,5,5 should be isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(5,7,3),'Scalene','5,7,3 should be scalene')
    def testScaleneTriangles2(self):
        self.assertEqual(classify_triangle(10,8,5),'Scalene','10,8,5 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()