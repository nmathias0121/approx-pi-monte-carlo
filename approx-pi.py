# Approximate the value of Pi using monte carlo simulation
import numpy

# test on different sample sizes & find the most accurate one
sample_size_lst = [10, 100, 1000, 10000, 25000, 40000]


# circle inside square with side = 1
# generate N (x,y) points in [0,1]
# generate uniformly distributed points (x, y) in [0, 1]
# if point inside circle, add point to list 
#   should satisfy condition (x-radius)^2) + (y-radius)^2) <= radius^2

# value of pi is (number of points on or inside the circle) / (total number of points)