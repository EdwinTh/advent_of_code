library(tidyverse)
d11 <- read_lines("data/data11") %>% str_split("") %>% 
  map2_dfr(1:length(.), ~tibble(val = .x, x = 1:length(.x), y = .y))

# star 1
mapping_one_pos <- function(x = 1, y = 1) {
  expand_grid(xa = c(x-1, x, x+1),  ya = c(y-1, y, y+1)) %>% 
    filter(!(xa == x & ya == y)) %>% 
    filter(xa > 0, xa <= max(d11$x), ya > 0, ya <= max(d11$y)) %>% 
    mutate(x = x, y = y)
}

mapping <- map2_dfr(d11$x, d11$y, mapping_one_pos)

update_vals <- function(df, mp, min_occ) {
  df %>% inner_join(mp, by = c('x', 'y')) %>% 
    inner_join(rename(df, vala = val), by = c('xa' = 'x', 'ya' = 'y')) %>% 
    group_by(x, y) %>% 
    summarise(adj_occ = sum(vala == "#"), 
              val     = min(val),
              .groups = "drop") %>% 
    mutate(new_val = case_when(
      val == "L" & adj_occ == 0       ~ "#",
      val == "#" & adj_occ > min_occ  ~ "L",
      TRUE                            ~ val
    )) %>% arrange(y, x)
}

update_all <- function(df, mp = mapping, min_occ = 3) {
  df <- update_vals(df, mp, min_occ)
  if (all(df$val == df$new_val)) return(df)
  update_all(df %>% select(val = new_val, x, y), mp, min_occ)
}

sum(update_all(d11, mapping, 3)$new_val == "#")

# star 2
mapping <- mapping %>% mutate(x = as.numeric(x), y = as.numeric(y))
all_adjacent <- inner_join(mapping, d11, by = c('xa' = 'x', 'ya' = 'y')) 

update_mapping <- function(aa) {
  new_mapping <- aa %>% 
    mutate(
      new_xa = if_else(val == ".", xa + sign(xa - x), xa),
      new_ya = if_else(val == ".", ya + sign(ya - y), ya),
      invalid_step = new_xa < 1 | new_xa > max(aa$x) | 
        new_ya < 1 | new_ya > max(aa$y),
      new_xa = if_else(invalid_step, xa, new_xa),
      new_ya = if_else(invalid_step, ya, new_ya),
      check_col = (new_xa == xa) & (new_ya = ya),
    )
  mapping_iter <- new_mapping %>% select(x, y, xa = new_xa, ya = new_ya)
  if (all(new_mapping$check_col)) return(mapping_iter)
  inner_join(mapping_iter, d11, by = c('xa' = 'x', 'ya' = 'y')) %>% 
    update_mapping()
}

mapping_2 <- update_mapping(all_adjacent)
sum(update_all(d11, mapping_2, 4)$new_val == "#")
