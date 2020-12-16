library(tidyverse); library(VeryLargeIntegers)
d13 <- read_lines("data/data13")

# star 1
ts <- as.numeric(d13[1])
ids <- str_split(d13[2], ",")[[1]] %>% .[.!= "x"] %>% as.numeric()
next_leave <- ids - ts %% ids
min(next_leave) * ids[which.min(next_leave)]

# star 2
id_full <- str_split(d13[2], ",")[[1]]
offsets <- which(id_full != "x") - 1

find_start_point <- function(b, o, sp, clcm, b_length = 10000, b_start = 0) {
  a_seq <- cumsum(c(sp, rep(clcm, b_length)))[b_start:b_length]
  opts <- a_seq[(a_seq + o) %in% seq(b, b*b_length, b)]
  if (length(opts) > 0) return(opts[1])
  find_start_point(b, o, sp, clcm,  b_length * 10, b_length)
}

current_lcm <- ids[1]
current_sp  <- ids[1]

for (i in 2:length(ids)) {
  current_sp <- find_start_point(ids[i], offsets[i], current_sp, current_lcm)
  print(current_sp)
  if (i == length(ids)) {
    print(current_sp + offsets[i])
    break
  }
  current_lcm <- pracma::Lcm(current_lcm, ids[i])
  print(i)
}

tmp <- function(a, b, o) {
  eer <- VeryLargeIntegers::exteuclid(a, b)
  bezouts <- c(eer[[2]]$sign * eer[[2]]$value, eer[[3]]$sign * eer[[3]]$value)
  nm <- bezouts * o
  abs(max(c(a, b) * abs(nm) - a*b))
}

