library(tidyverse)
d16 <- read_lines("data/data16")
d16 <- split(d16, cumsum(d16 == ""))

# star 1 
valid_vals <- d16[[1]] %>% str_extract_all("\\d+-\\d+") %>% unlist() %>% 
  str_replace_all("-", ":") %>% map(~eval(parse(text = .x))) %>% unlist()

str_extract_all(d16[[3]][-c(1,2)], "\\d+") %>% 
  map(~setdiff(as.numeric(.x), valid_vals)) %>% unlist() %>% sum()

# star 2
other_tickets <- str_extract_all(d16[[3]][-c(1,2)], "\\d+") %>% 
  map(as.numeric)
str_extract_all(d16[[3]][-c(1,2)], "\\d+") %>% 
  map_lgl(~setdiff(as.numeric(.x), valid_vals) %>% length() %>% `==`(0))
