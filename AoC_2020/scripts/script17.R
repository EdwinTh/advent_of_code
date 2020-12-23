library(tidyverse)
d17 <- read_lines("data/data17") %>% str_split("") %>% map(~as.numeric(.x == "#")) %>% 
  map2_dfr(1:length(.), ~tibble(x = 1:length(.x), y = .y, z = 0, val = .x))

# star 1
expand_range <- function(x, w = 1) (min(x)-w):(max(x)+w)
expand_df <- function(x, w = 1) {
  expand_grid(x = expand_range(x$x, w), 
              y = expand_range(x$y, w), 
              z = expand_range(x$z, w))
}

make_mapping_table <- function(new_x) {
  split(new_x, rownames(new_x)) %>% 
    map_dfr(~expand_df(.x) %>% rename(xa = x, ya = y, za = z) %>% 
            bind_cols(.x) %>% filter(!(xa == x & ya == y & za == z)))
}
mapping_table <- expand_df(d17, w = 6) %>% make_mapping_table()

one_cycle <- function(x) {
  expand_df(x) %>% 
    inner_join(mapping_table, by = c("x", "y", "z")) %>% 
    left_join(x, by = c("xa" = "x", "ya" = "y", "za" = "z")) %>% 
    group_by(x, y, z) %>% 
    summarise(vala = sum(val, na.rm = TRUE), .groups = "drop") %>% 
    left_join(x, by = c("x", "y", "z")) %>% padr::fill_by_value() %>% 
    mutate(val = as.numeric( (val & vala %in% 2:3) | (!val & vala == 3))) %>% 
    select(-vala)
}

repeat_cycle <- function(x, l = 6) {
  if (l == 0) return(x)
  repeat_cycle(one_cycle(x), l -1)
}
repeat_cycle(d17)$val %>% sum()

# star 2
d17 <- read_lines("data/data17") %>% str_split("") %>% map(~as.numeric(.x == "#")) %>% 
  map2_dfr(1:length(.), ~tibble(x = 1:length(.x), y = .y, z = 0, w = 0, val = .x))

expand_range <- function(x, wt = 1) (min(x)-wt):(max(x)+wt)
expand_df <- function(x, wt = 1) {
  expand_grid(x = expand_range(x$x, wt), 
              y = expand_range(x$y, wt), 
              z = expand_range(x$z, wt),
              w = expand_range(x$w, wt))
}

make_mapping_table <- function(new_x) {
  split(new_x, rownames(new_x)) %>% 
    map_dfr(~expand_df(.x) %>% rename(xa = x, ya = y, za = z, wa = w) %>% 
              bind_cols(.x) %>% filter(!(xa == x & ya == y & za == z & wa == w)))
}
mapping_table <- expand_df(d17, wt = 6) %>% make_mapping_table()

one_cycle <- function(x) {
  expand_df(x) %>% 
    inner_join(mapping_table, by = c("x", "y", "z", "w")) %>% 
    left_join(x, by = c("xa" = "x", "ya" = "y", "za" = "z", "wa" = "w")) %>% 
    group_by(x, y, z, w) %>% 
    summarise(vala = sum(val, na.rm = TRUE), .groups = "drop") %>% 
    left_join(x, by = c("x", "y", "z", "w")) %>% padr::fill_by_value() %>% 
    mutate(val = as.numeric( (val & vala %in% 2:3) | (!val & vala == 3))) %>% 
    select(-vala)
}

repeat_cycle <- function(x, l = 6) {
  if (l == 0) return(x)
  repeat_cycle(one_cycle(x), l -1)
}
repeat_cycle(d17)$val %>% sum()
