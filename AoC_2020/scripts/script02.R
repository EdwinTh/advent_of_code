library(tidyverse)
d2 <- readLines("data/data02")

# star 1
spl <- d2 %>% str_split(" ")
from_to <- map_chr(spl, 1) %>% str_split("-") %>% map(as.numeric)
char    <- map_chr(spl, 2) %>% str_replace(":", "")
pattern <- map_chr(spl, 3) %>% str_split("")
times_char_in_pattern <- map2_int(char, pattern, ~sum(.x == .y))
map2_lgl(from_to, times_char_in_pattern, ~.x[1] <= .y & .x[2] >= .y) %>% sum()

# star 2
pattern_at_position <- map2(from_to, pattern, ~c(.y[.x[1]], .y[.x[2]]))
map2_lgl(char, pattern_at_position, ~sum(.x == .y) == 1) %>% sum()
