# -*- coding: utf-8 -*-
"""
Updated sep 21, 2022
The primary goal of this file is to demonstrate a simple python program to classify
triangles
@author: rao
@author: pranav
"""


def classify_triangle(side_a, side_b, side_c):
    '''
    Classify Triangle
    '''
    instance_list = [isinstance(side_a, int), isinstance(side_b, int), isinstance(side_c, int)]
    if (max(side_a, side_b, side_c) > 200 or
            min(side_a, side_b, side_c) < 0 or
            not instance_list):
        return 'InvalidInput'

    if ((side_a >= (side_b + side_c)) or
            (side_b >= (side_a + side_c)) or
            (side_c >= (side_a + side_b))):
        return 'NotATriangle'

    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    elif ((((side_a ** 2) + (side_b ** 2)) == (side_c ** 2)) or
          (((side_a ** 2) + (side_c ** 2)) == (side_b ** 2)) or
          (((side_c ** 2) + (side_b ** 2)) == (side_a ** 2))):
        return 'Right'
    elif (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isoceles'