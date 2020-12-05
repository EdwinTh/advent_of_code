library(tidyverse)
d5 <- readLines("data/data05") 

# star 1 
rows_input <- str_sub(d5, 1, 7) %>% str_replace_all("F", "0") %>% 
  str_replace_all("B", "1") %>% str_split("") %>% map(as.numeric)

rows <- matrix(unlist(rows_input), byrow = TRUE, nrow = length(rows_input)) %*%
  matrix(c(64, 32, 16, 8, 4, 2, 1)) %>% as.numeric()

seats_input <- str_sub(d5, 8, 10) %>% str_replace_all("L", "0") %>% 
  str_replace_all("R", "1") %>% str_split("") %>% map(as.numeric)

seats <- matrix(unlist(seats_input), byrow = TRUE, nrow = length(seats_input)) %*%
  matrix(c(4, 2, 1)) %>% as.numeric()

max(rows * 8 + seats)

# star 2
my_row <- tibble(rows = rows) %>% count(rows) %>% 
  filter(!rows %in% range(rows), n != 8) %>% pull(rows)
my_seat <- setdiff(0:7, seats[rows == my_row])

my_row * 8 + my_seat