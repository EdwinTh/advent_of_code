library(tidyverse)

adv13 <- readLines("data/advent_data13")
rows  <- length(adv13); cols <- nchar(adv13[1])
lookup <- c(0, 1, 1, 1, 2, 2, 2, 3:5)
names(lookup) <- c(" ", "|", "^", "v", "-", ">", "<", "/", "\\", "+")

grid_mat <- lookup[adv13 %>% str_split("") %>% unlist()] %>% 
  matrix(nrow = rows, ncol = cols, byrow = TRUE)
  
coord_change_no_junction <- function(direction, 
                                     rail){
  # directions: 1 up 2 down 3 left 4 right
  # rail: 1 | 2 - 3 / 4 \
  delta <- tribble(
    ~dir,        ~rl, ~x_delta, ~y_delta,
    1,           1,    0,        -1,      
    1,           3,    1,         0,
    1,           4,    -1,        0,
    2,           1,    0,         1,
    2,           3,    -1,        0,
    2,           4,    1,         0,
    3,           2,    -1,        0,
    3,           3,    0,         -1,
    3,           4,    0,         1,
    4,           2,    1,         0,
    4,           3,    0,         1,
    4,           4,    0,         -1
  )
  delta_row <- delta %>% filter(dir == direction, rl == rail)
  if (nrow(delta_row) == 0) {
    stop("You made a thinking error, mister!")
  }
  delta_row
}

coord_change_junction <- function(direction,
                                  cart_state) {
  # directions: 1 up 2 down 3 left 4 right
  # cart state 1 left 2 straight 3 right
  delta <- tribble(
    ~dir, ~state, ~x_delta, ~y_delta,
    1,     1,     -1,       0, 
    1,     2,      0        -1,
    1,     3,      1,       0,
    2,     1,      1,       0,
    2,     2,      0,       1,
    2,     3,      -1,      0,
    3,     1,      0,       1,
    3,     2,      -1,      0,
    3,     3,      0,       -1,
    4,     1,      0,       -1,
    4,     2,      1,       0,
    4,     3,      0,       1
  )
  delta_row <- delta %>% filter(dir == direction, state == cart_state)
  if (nrow(delta_row) == 0) {
    stop("You made a thinking error, mister!")
  }
  delta_row
}
