library(tidyverse)
adv6 <- read_delim("data/advent_data6", 
                   delim = ", ",
                   col_names = FALSE) %>% 
  rename(x = X1, y = X2) %>% 
  mutate(y = as.numeric(y))


pl <- ggplot(adv6, aes(x, y)) + geom_point()

manhattan <- function(x1, y1, x2, y2) 
  abs(x1 - x2) + abs(y1 - y2)

## Part 1
full_x_range <- (min(adv6$x)-100) : (max(adv6$x) + 100)
full_y_range <- (min(adv6$y)-100) : (max(adv6$y) + 100)
all_grid_points <- expand.grid(full_x_range, full_y_range) %>% 
  as_data_frame() %>% 
  rename(x = Var1, y = Var2)

all_dists <- map2(adv6$x, adv6$y,
                  ~manhattan(.x, .y, all_grid_points$x, all_grid_points$y)) %>% 
  bind_cols(all_grid_points, .) %>% 
  gather(key = ref_point, value = manhat, -x, -y)

closest <- all_dists %>% 
  group_by(x, y) %>% 
  filter(manhat == min(manhat)) %>% 
  filter(n() == 1) %>% 
  ungroup()

pl + 
  geom_point(data = closest %>% filter(ref_point == "V26"), col = "red", alpha = .01) +
  geom_point(data = closest %>% filter(ref_point == "V6"), col = "blue", alpha = .01) +
  geom_point(data = closest %>% filter(ref_point == "V1"), col = "green", alpha = .01)

# so we toke a wide border relatively to the range. We are sure 
# that everything that touches the border here take off to infinity.
going_to_inf <- closest %>% 
  filter(x == min(full_x_range) |
         x == max(full_x_range) |
         y == min(full_y_range) |
         y == max(full_y_range))

pl +
  geom_point(data = going_to_inf, aes(col = ref_point))

not_inf <- anti_join(closest, going_to_inf %>% select(ref_point))

not_inf %>% 
  count(ref_point, sort = TRUE) %>% 
  slice(1) %>% 
  pull(n)

pl + 
  geom_point(data = not_inf, aes(col = ref_point), alpha = .05)

## Part 2
all_dists %>% 
  group_by(x, y) %>% 
  summarise(tot_manhat = sum(manhat)) %>% 
  filter(tot_manhat < 10000) %>% 
  nrow()
