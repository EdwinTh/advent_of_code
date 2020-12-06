library(tidyverse)
d6 <- readLines("data/data06") %>% 
  split(cumsum(. == "")) %>% map(~.x[.x != ""])

# star 1
d6 %>% 
  map_dbl(~paste(.x, collapse = "") %>% str_split("") %>% unlist() %>%
            unique %>% length) %>% sum()

# star 2
psg <- map_dbl(d6, length)
ltr_count <- d6 %>% 
  map(~paste(.x, collapse = "") %>% str_split("") %>% unlist() %>% table())
map2_dbl(psg, ltr_count, ~sum(.x == .y)) %>% sum()