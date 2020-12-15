library(tidyverse)
d12 <- read_lines("~/Desktop/data12")
dirs  <- str_extract(d12, "[A-Z]")
steps <- str_extract(d12, "\\d+") %>% as.numeric()

# star 1
update_pos <- function(p, dir, step, f) {
  switch(dir,
         N = c(p[1], p[2] + step),
         S = c(p[1], p[2] - step),
         E = c(p[1] + step, p[2]),
         W = c(p[1] - step, p[2]),
         "F" = f * step + pos
  )
}

update_facing <- function(f, dir, step) {
  wheel <- tibble(one = c(-1, 0, 1, 0), two = c(0, 1, 0, -1), pos = 1:4)
  pos_on_wheel <- wheel %>% filter(one == f[1] & two == f[2]) %>% pull(pos)
  new_pos <- if_else(dir == "R", pos_on_wheel + step / 90, pos_on_wheel - step / 90)
  new_pos <- if_else(new_pos < 1, 4 + new_pos,
                     if_else(new_pos > 4, new_pos - 4, new_pos))
  unlist(wheel %>% filter(pos == new_pos))[c(1, 2)]
}

facing <- c(1, 0)
pos    <- c(0, 0)

for (i in seq_along(steps)) {
  if (dirs[i] %in% c("R", "L")) {
    facing <- update_facing(facing, dirs[i], steps[i])
  } else {
    pos <- update_pos(pos, dirs[i], steps[i], facing)
  }
}
sum(abs(pos))

# star 2
update_pos <- function(pos, step, wp) {
  pos + wp * step
}

update_waypoint <- function(wp, dir, step) {
  switch(dir,
         N = c(wp[1], wp[2] + step),
         S = c(wp[1], wp[2] - step),
         E = c(wp[1] + step, wp[2]),
         W = c(wp[1] - step, wp[2]),
         L = rotate_wp(wp, dir, step),
         R = rotate_wp(wp, dir, step)
  )
}

rotate_wp <- function(wp, dir, step) {
  if (step == 180) {
    wp * -1
  } else if ((step == 90 & dir == "R") | (step == 270 & dir == "L")) {
    c(wp[2], -wp[1])
  } else {
    c(-wp[2], wp[1])
  }
  
  waypoint <- c(10, 1)
  pos      <- c(0, 0)
  
  for (i in seq_along(dirs)) {
    if (dirs[i] == "F") {
      pos <- update_pos(pos, steps[i], waypoint)
    } else {
      waypoint <- update_waypoint(waypoint, dirs[i], steps[i])
    }
  }
  abs(pos) %>% sum()
}