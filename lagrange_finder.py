from vpython import *
from math import sqrt

"""
The function finds the lagrange points from the 2 stars.

INPUTS:
vector of star 1
vector of star 2

OUTPUTS:
vector of L1
vector of L2
vector of L3
vector of L4
vector of L5
"""

# Notes:
# temp = vec(10, 20, 30)
# temp.x = 10.0, etc

def lagrange_finder(star_1, star_2):
    # Find lagrange point 1
    
    # Find lagrange point 2
    
    # Find lagrange point 3 (opposite the point of star_2)
    lp2 = -star_2

    # Find lagrange point 4 (equilateral triangle)
    # Find halfway point between the two
    length = star_2.x - star_1.x
    halfway = length/2 
    height = length*sqrt(3)/2
    lp4 = vec(halfway, height, 0)
    print(lp4)
    

    # Find lagrange point 5 (equilateral triangle)

    return lp2, lp4
if __name__ == '__main__':
    print("Running test case")
    star_1 = vec(0, 0, 0)
    star_2 = vec(10, 10, 0)
    l2, l4 = lagrange_finder(star_1, star_2)
    first = sphere(pos = star_1, radius = 1, color = color.green)
    second = sphere(pos = star_2, radius = 1, color = color.red)
    l2 = sphere(pos = l2, radius = 1, color = color.blue)
    l4 = sphere(pos = l4, radius = 1, color = color.orange)

