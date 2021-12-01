# star 1
nrs <- readLines("~/Documents/advent_of_code/AoC_2021/day_1/data.txt") |>
  as.integer()

print(sum(nrs[-1] > nrs[-length(nrs)]))

# star 2
l <- length(nrs)
nrs_sum <- nrs[-c(1:2)] + nrs[-c(1, l)] + nrs[-c(l-1, l)]
print(sum(nrs_sum[-1] > nrs_sum[-length(nrs_sum)]))