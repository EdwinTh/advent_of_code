library(tidyverse)
d12 <- readLines('/data/data12')

# star 1
str_extract_all(d12, "-?\\d+")[[1]] %>% as.numeric() %>% sum()

# star 2
d12 <- jsonlite::read_json("~/Desktop/tmp.json")

d12 %>% length()
