sample_size_lst <- list(10, 100, 1000, 10000, 25000, 40000)

for (N in sample_size_lst) {
    lst_points_inside_circle <- list()
    num <- 0

    for (i in 1:N) {
        # generate uniform distributed points (x, y) in [0,1]
        x <- runif(1, 0, 1)
        y <- runif(1, 0 ,1)

        # if point inside circle
        if (((x-0.5)^2 + (y-0.5)^2) <= 0.5 ^ 2) {
            lst_points_inside_circle <- append(lst_points_inside_circle, list(x,y))
            num = num + 1
        }
    }
    
    # approximate value of pi
    pi_approx <- 4 * (num / N)
    print(paste("for sample size ", N, " approx value of pi is ", pi_approx, " difference is ", pi - pi_approx))

}
