library(tidyverse)

calculate_house <- function(nr, stop_val = 33100000) {
  score <- sum(1:nr[nr %% 1:nr == 0] * 10)
  if (score > stop_val) return(nr)
  calculate_house(nr + 1, stop_val)
}

calculate_house(1, stop_val = 33100000)


  