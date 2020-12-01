library(tidyverse)
library(stringr)
adv10 <- readLines("data/advent_data10")
adv10_df <- adv10 %>% str_split("<|>|,") %>% 
  map_df(~data_frame(x = as.numeric(.x[2]), 
                     y = as.numeric(.x[3]),
                     x_speed = as.numeric(.x[5]),
                     y_speed = as.numeric(.x[6])))

# it is going to take approx. 10k steps
adv10_df %>% mutate(x / x_speed, y / y_speed) %>% apply(2, max)
secs <- 10580
getting_close <- 
  adv10_df %>% mutate(x = x + x_speed * secs, 
                      y = y + y_speed * secs)

update_df <- function(df, base = 10) {
  df %>% mutate(x = x + x_speed * base,
                y = y + y_speed * base)
}


getting_close <- update_df(getting_close, 1) 
ggplot(getting_close, aes(x, y)) + geom_point(shape = 15, size = 5)
secs <- secs + 1
secs