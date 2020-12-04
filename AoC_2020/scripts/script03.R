library(tidyverse)
d3 <- readLines("data/data03")

# part 1
input_to_mat <- function(x) {
 nrs <- map(str_split(x, ""), ~as.numeric(.x == "#"))
 matrix(unlist(nrs), nrow = length(nrs), byrow = TRUE)
}

expand_till_wide_enough <- function(x, f) {
  if ((nrow(x) * f) <= ncol(x)) return(x)
  expand_till_wide_enough(cbind(x, x), f)
}

extract_pattern <- function(x, down_step, right_step) {
  x_ind <- seq(1, by = down_step, length.out = nrow(x)) 
  y_ind <- seq(1, by = right_step, length.out = nrow(x))
  x_ind <- x_ind[x_ind <= nrow(x)]
  y_ind <- y_ind[1:length(x_ind)]
  map2_dbl(x_ind, y_ind, ~x[.x, .y])
}

d3 %>% input_to_mat() %>% expand_till_wide_enough(3) %>% extract_pattern(1, 3) %>% sum()

# part 2
full_seq <- function(x, down_step, right_step) {
  input_to_mat(x) %>% 
    expand_till_wide_enough(right_step) %>% 
    extract_pattern(down_step, right_step) %>% 
    sum()
}

full_seq(d3, 1, 1) * full_seq(d3, 1, 3) * full_seq(d3, 1, 5) *
  full_seq(d3, 1, 7) * full_seq(d3, 2, 1)
