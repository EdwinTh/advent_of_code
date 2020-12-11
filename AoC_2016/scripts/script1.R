library(tidyverse)
d1 <- read_lines("data/data01") %>% str_split(", ") %>% unlist()
dir <- str_extract_all(d1, "L|R") %>% unlist()
steps <- str_extract_all(d1, "\\d+") %>% unlist() %>% as.numeric()

# star 1
change_dir <- function(cur_dir, dir_iter) {
  if (cur_dir == "up") return(ifelse(dir_iter == "L", "left", "right"))
  if (cur_dir == "right") return(ifelse(dir_iter == "L", "up", "down"))
  if (cur_dir == "down") return(ifelse(dir_iter == "L", "right", "left"))
  if (cur_dir == "left") return(ifelse(dir_iter == "L", "down", "up"))
}

change_coord <- function(coord, cur_dir, steps_iter) {
  if (cur_dir == "up") coord[2] <- coord[2] + steps_iter
  if (cur_dir == "down") coord[2] <- coord[2] - steps_iter
  if (cur_dir == "left") coord[1] <- coord[1] - steps_iter
  if (cur_dir == "right") coord[1] <- coord[1] + steps_iter
  coord
}

coord <- c(0, 0)
cur_dir <- "up"
for (i in seq_along(dir)) {
  cur_dir <- change_dir(cur_dir, dir[i])
  coord <- change_coord(coord, cur_dir, steps[i])
}
abs(coord) %>% sum()

# star 2
coord <- c(0, 0)
cur_dir <- "up"
coord_visited <- tibble(one = 0, two = 0)
i <- 1
while (nrow(coord_visited) == nrow(distinct(coord_visited))) {
  cur_dir <- change_dir(cur_dir, dir[i])
  new_coord <- change_coord(coord, cur_dir, steps[i])
  coord_visited_iter <- tibble(one = coord[1]:new_coord[1], 
                               two = coord[2]:new_coord[2])[-1, ]
  coord_visited <- bind_rows(coord_visited, coord_visited_iter)
  i <- i + 1
  coord <- new_coord
}
coord_visited %>% count(one, two, sort = TRUE)
8 + 158
