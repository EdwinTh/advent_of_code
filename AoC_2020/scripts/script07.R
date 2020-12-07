library(tidyverse)
library(glue)
d7 <- readLines("data/data07")

# star 1
d7_itm <- d7 %>% str_replace_all("bags|bag|\\.", "") %>% 
  str_split("contain")
from <- map_chr(d7_itm, ~.x[1] %>% str_trim())
to   <- map(d7_itm, ~.x[2] %>% str_split(",") %>% unlist %>%  str_trim)

to_df <- function(from_el, to_el) {
  to_nr <- as.numeric(str_extract(to_el, "\\d+"))
  to_nm <- str_replace(to_el, "\\d+", "") %>% str_trim()
  tibble(from = from_el, to = to_nm, nr = to_nr)
}

d7_df <- map2_dfr(from, to, to_df) %>%
  mutate(to = ifelse(to == "no other", NA, to))

top <- d7_df[!d7_df$from %in% d7_df$to, ]
names(top) <- paste0(names(top), "0")

add_layer <- function(x, y, iter = 1) {
  names(y) <-  c(glue("to{iter-1}"), glue("to{iter}"), glue("nr{iter}"))
  left_join(x, y)
}

x <- top
reached_end <- FALSE
i <- 1 
while(!reached_end) {
  x <- add_layer(x, d7_df, i)
  reached_end <- x %>% pull() %>% is.na %>% all
  i <- i + 1
}

all_before_shiny_gold <- function(x) {
  if ("shiny gold" %in% x) {
    x[1:(which(x == "shiny gold") - 1)]
  } else {
    NULL
  }
}

split(x %>% select("from0", starts_with("to")), 1:nrow(x)) %>% 
  map(unlist) %>% 
  map(all_before_shiny_gold) %>% 
  unlist() %>% unique() %>% length()
  
# star 2
sg <- x[x %>% apply(1, function(x) any(x == "shiny gold", na.rm = T)), ]
sum(sg$from0 == "shiny gold")

colSums(sg == "shiny gold", na.rm = T)
sg_ss <- sg %>% filter(to10 == "shiny gold") %>% 
  select(to11:nr16)


get_bags <- function(x) x %>% select_if(is.numeric) %>% apply(1, prod) %>% sum()
nr16 <- sg_ss %>% filter(!is.na(nr16)) %>% get_bags()
nr15 <- sg_ss %>% select(to11:nr15) %>% filter(!is.na(nr15)) %>% distinct() %>% get_bags()
nr14 <- sg_ss %>% select(to11:nr14) %>% filter(!is.na(nr14)) %>% distinct() %>% get_bags()
nr13 <- sg_ss %>% select(to11:nr13) %>% filter(!is.na(nr13)) %>% distinct() %>% get_bags()
nr12 <- sg_ss %>% select(to11:nr12) %>% filter(!is.na(nr12)) %>% distinct() %>% get_bags()
nr11 <- sg_ss %>% select(to11:nr11) %>% filter(!is.na(nr11)) %>% distinct() %>% get_bags()
nr16 + nr15 + nr14 + nr13 + nr12 + nr11
