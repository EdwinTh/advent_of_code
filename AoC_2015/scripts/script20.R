library(tidyverse)

calculate_house <- function(nr, stop_val = 33100000, step_size = 1) {
  score <- sum((1:nr)[(nr %% (1:nr)) == 0] * 10)
  print(nr)
  if (score > stop_val) return(nr)
  calculate_house(nr + step_size, stop_val, step_size = step_size)
}

