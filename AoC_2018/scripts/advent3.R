adv3 <- readLines("data/advent_data3")
library(stringr)
library(tidyverse)

## Part 1
clean_string <- function(x) {
 splitted <- str_split(x, " ") 
 start_point <- map_chr(splitted, 3) 
 pixels      <- map_chr(splitted, 4) 
 
 bind_cols(
   
 start_point %>% str_split(",|:") %>% 
   map_df(~data_frame(x_start = as.integer(.x[1]), 
                      y_start = as.integer(.x[2]))),
 
 pixels %>% str_split("x") %>% 
   map_df(~data_frame(x_pix = as.integer(.x[1]),
                      y_pix = as.integer(.x[2])))
 )
}

info_df <- clean_string(adv3)

get_all_pixels <- function(x_start, y_start, x_len, y_len) {
  x_ind <- (x_start + 1):(x_start + x_len)
  y_ind <- (y_start + 1):(y_start + y_len)
  expand.grid(x_ind, y_ind) %>% 
    as_data_frame() %>% 
    rename(x = Var1, y = Var2) 
}

all_pixels_df <- pmap_df(list(info_df$x_start, 
                              info_df$y_start, 
                              info_df$x_pix, 
                              info_df$y_pix),
                      get_all_pixels) 

count(all_pixels_df, x, y) %>% 
  filter(n > 1) %>% 
  nrow()

## Part 2
all_pixels_list <- pmap(list(info_df$x_start, 
                             info_df$y_start, 
                             info_df$x_pix, 
                             info_df$y_pix),
                         get_all_pixels) 

all_pixels_df_nr <- map2_df(all_pixels_list,
                            1:length(all_pixels_list), 
                            ~mutate(.x, id = .y))

pixels <- all_pixels_df_nr %>% count(id)

blown_up <- inner_join(all_pixels_df,
                       all_pixels_df_nr)
blown_join <- blown_up %>% count(id)
inner_join(pixels, blown_join)
