library(tidyverse)
d17 <- c(43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38)

# star1
map_dbl(1:20, ~combn(d17, .x) %>% colSums() %>% `==`(150) %>% sum) %>% sum()

#star 2
map_dbl(1:20, ~combn(d17, .x) %>% colSums() %>% `==`(150) %>% sum)

