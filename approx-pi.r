sample_size_lst <- list(10, 100, 1000, 10000, 25000, 40000)

for (N in sample_size_lst) {
    for (i in 1:N) {
        # generate uniform distributed points (x, y) in [0,1]
        x <- runif(1, 0, 1)
        y <- runif(1, 0 ,1)

        cat("y is ", y, "\n")
    }
}