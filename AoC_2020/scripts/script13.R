library(tidyverse)
d13 <- read_lines("data/data13")

# star 1
ts <- as.numeric(d13[1])
ids <- str_split(d13[2], ",")[[1]] %>% .[.!= "x"] %>% as.numeric()
next_leave <- ids - ts %% ids
min(next_leave) * ids[which.min(next_leave)]

# star 2
id_full <- str_split(d13[2], ",")[[1]]
offsets <- which(id_full != "x") - 1

get_possible_range <- function(b, offset) {
  range_a <- seq(ids[1], ids[1] * 10000, ids[1]) + offset
  range_b <- seq(b, b * 10000, b)
  strt <- intersect(range_a, range_b) %>% min() - offset
  cumsum(c(strt, rep(pracma::Lcm(ids[1], b), 1e9)))
}

pr <- map2(ids[-1], offsets[-1], get_possible_range)
find_smallest_intersect <- function(l) {
  if (length(l) == 1) return(min(l[[1]]))
  l[[1]] <- intersect(l[[1]], l[[2]])
  find_smallest_intersect(l[-2])
} 
find_smallest_intersect(pr) + max(offsets)
