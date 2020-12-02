library(tidyverse)
d15 <- readLines("/data/data15")

# star 1
m1  <- matrix(unlist(map(str_extract_all(d15, "-?\\d+"), as.numeric)), nrow = 4, byrow = TRUE)[, -5]
all_combs <- expand_grid(a = 0:100, b = 0:100, c = 0:100, d = 0:100)
all_combs <- all_combs[rowSums(all_combs) == 100, ]
mult <- t(m1) %*% t(all_combs)
mult_sel <- mult[ ,apply(mult, 2, function(col) !any(col < 0))]
max(apply(mult_sel, 2, prod))

# star 2
cals   <- matrix(unlist(map(str_extract_all(d15, "-?\\d+"), as.numeric)), nrow = 4, byrow = TRUE)[, 5, drop = F]
cal500 <- mult[ , which(as.numeric(t(cals) %*% t(all_combs)) == 500)]
cal500_sel <- cal500[ ,apply(cal500, 2, function(col) !any(col < 0))]
max(apply(cal500_sel, 2, prod))
