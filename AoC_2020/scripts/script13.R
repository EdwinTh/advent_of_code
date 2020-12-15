library(tidyverse); library(pracma)
d13 <- read_lines("~/Desktop/data13")

# star 1
ts <- as.numeric(d13[1])
ids <- str_split(d13[2], ",")[[1]] %>% .[.!= "x"] %>% as.numeric()
next_leave <- ids - ts %% ids
min(next_leave) * ids[which.min(next_leave)]

# star 2
id_full <- str_split(d13[2], ",")[[1]]
offsets <- which(id_full != "x") - 1

find_start_point <- function(b, o, sp, clcm, b_length = 100, b_start = 0) {
  a_seq <- cumsum(c(sp, rep(clcm, b_length)))[b_start:b_length]
  print(b_length)
  opts <- a_seq[(a_seq + o) %in% seq(b, b*b_length, b)]
  if (length(opts) > 0) return(opts[1])
  find_start_point(b, o, sp, clcm,  b_length * 10, b_length)
}

current_lcm <- ids[1]
current_sp  <- ids[1]

for (i in 2:length(ids)) {
  current_sp <- find_start_point(ids[i], offsets[i], current_sp, current_lcm)
  if (i == length(ids)) {
    print(current_sp + offsets[i])
    break
  }
  current_lcm <- Lcm(current_lcm, ids[i])
  print(i)
}

library()