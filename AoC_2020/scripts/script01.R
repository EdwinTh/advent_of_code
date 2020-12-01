library(tidyverse)
d1 <- readLines("data/data01") %>% as.numeric()

# star 1
expand_grid(n1 = d1, n2 = d1) %>% 
  filter(n1 + n2 == 2020) %>% 
  summarise(n1 * n2) 
             
# star 2
expand_grid(n1 = d1, n2 = d1, n3 = d1) %>% 
  filter(n1 + n2 + n3 == 2020) %>% 
  summarise(n1 * n2 * n3)
