library(tidyverse)

grid <- expand.grid(1:300, 1:300) %>% 
  as_data_frame() %>% 
  rename(x = Var1, y = Var2)

add_fuel_levels <- function(serial_nr) {
  grid %>% 
    mutate(step1 = ((x + 10) * y + serial_nr) * (x + 10)) %>% 
    mutate(fuel = floor(step1 / 100) %>% 
             str_sub(-1, -1) %>% as.numeric %>% `-`(5))
}

grid <- add_fuel_levels(5235)

# Part 1
all_3_by_3 <- function(grid) {
  square_dim <- grid %>% select(x, y) %>% 
    filter(x < 298, y < 298) %>% 
    mutate(x_end = x + 2, y_end = y + 2) %>% 
    mutate(x_square = map2(x, x_end, ~.x:.y),
           y_square = map2(y, y_end, ~.x:.y)) %>% 
    mutate(all_ind  = map2(x_square, y_square, 
                           ~expand.grid(unlist(.x), unlist(.y)))) %>% 
    select(x, y, all_ind)
  tidyr::unnest(square_dim) %>% 
    select(x_st = x, y_st = y, x = Var1, y = Var2)
}

base_grids <- all_3_by_3(grid)
fuel_by_square <- inner_join(grid, 
           base_grids) %>% 
  group_by(x_st, y_st) %>% 
  summarise(total_fuel = sum(fuel))
fuel_by_square %>% arrange(desc(total_fuel))

## Part 2
mat <- matrix(0, 298, 298)
for (i in 1:298) {
  for (j in 1:298) {
    mat[i, j] <- grid %>% 
      filter(x %in% c(i:(i+2)), y %in% c(j:(j+2))) %>% 
      pull(fuel) %>% 
      sum()
  }
}
# way too slow

fuel_mat <- matrix(grid$fuel, nrow = 300)
create_collection_mat <- function(sq_size) {
  base_mat <- matrix(0, 300, 300)
  for (i in 1:(300 - sq_size + 1)) {
    base_mat[i:(i + sq_size -1), i] <- rep(1, sq_size)
  }
  base_mat
}

xy <- expand.grid(1:300, 1:300) %>% 
  mutate(xy = paste(Var1, Var2, sep = "-")) %>% 
  pull(xy)
ind_mat<- matrix(xy, 300, 300)

max_fuel_val <- function(sq_size) {
  base_mat <- create_collection_mat(sq_size)
  all_squares <- t(fuel_mat %*% base_mat) %*% base_mat %>% t()
  data_frame(sq_size = sq_size, 
             ind     = ind_mat[all_squares == max(all_squares)], 
             max_val = max(all_squares))
}

all_values <- map_df(1:300, max_fuel_val)
all_values %>% arrange(desc(max_val))


