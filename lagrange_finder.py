from vpython import *

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
    halfway = star_2.x - star_1.x
    print(halfway)

    # Find lagrange point 5 (equilateral triangle)

    return lp2
if __name__ == '__main__':
    print("Running test case") 
    lagrange_finder(vec(10, 20, 30), vec(20, 40, 70))
