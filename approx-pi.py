# Approximate the value of Pi using monte carlo simulation
import numpy
import math

# test on different sample sizes & find the most accurate one
sample_size_lst = [10, 100, 1000, 10000, 25000, 40000]

# circle inside square with side = 1
for N in sample_size_lst:
    num_points_inside_circle = 0
    points_inside_circle = []

    # generate N (x,y) points in [0,1]
    for i in range(N):
        # generate uniformly distributed points (x, y) in [0, 1]
        x = numpy.random.uniform(0, 1)
        y = numpy.random.uniform(0, 1)

        # radius of circle = 0.5
        # if point inside circle
        if numpy.sqrt((x-0.5)**2 + (y-0.5)**2) <= 0.5 :
            # add point to list 
            points_inside_circle.append((x,y))
            num_points_inside_circle += 1

    pi_approx = 4 * (num_points_inside_circle / float(N))
    print("Pi is approximately ", pi_approx, "when sample size is ", N)

    diff = math.pi - pi_approx
    print("Difference between approximated pi & built-in value of pi is ", diff)