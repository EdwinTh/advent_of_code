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
keep <- map_lgl(other_tickets, ~setdiff(as.numeric(.x), valid_vals) %>% 
                  length() %>% `==`(0))
other_tickets <- other_tickets[keep]

ranges <- d16[[1]] %>% str_extract_all("\\d+-\\d+") %>%
  map(~.x %>% str_replace_all("-", ":") %>% paste0(collapse = ",")) %>% 
  map(~glue::glue("c({.x})")) %>% map(~eval(parse(text = .x)))
nm_ranges <- str_split(d16[[1]], ':') %>% map_chr(1)

ranges_df <- map2_dfr(ranges, nm_ranges, ~tibble(class = .y, val = .x))
ot_df     <- map_dfr(other_tickets, ~tibble(pos = 1:20, val = .x))
opts <- inner_join(ranges_df, ot_df) %>% 
  count(pos, class) %>% filter(n == 190)

assign_class <- function(assigned, opts) {
  if (all(assigned != "")) return(assigned)
  classes_one_opt <- opts %>% count(class) %>% filter(n == 1) %>% select(-n)
  to_assign <- inner_join(classes_one_opt, opts, by = "class")
  assigned[to_assign$pos] <- to_assign$class
  opts <- opts %>% filter(pos != to_assign$pos)
  assign_class(assigned, opts)
}

dep_pos <- which(assign_class(character(20), opts) %>% str_sub(1, 3) == "dep")
my_ticket <- d16[[2]][3] %>% str_split(",") %>% unlist() %>% as.numeric()
my_ticket[dep_pos] %>% prod()