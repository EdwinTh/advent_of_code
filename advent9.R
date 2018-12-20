library(tidyverse)

add_marble <- function(info_list, new_val) {
  append_pos <- info_list$current_pos + 1
  if (append_pos > length(info_list$circle)) append_pos <- 1
  info_list$circle <- append(info_list$circle, new_val, append_pos)
  info_list$current_pos <- append_pos + 1
  info_list
}

get_score <- function(i, info_list) {
  circle <- info_list$circle
  pos_to_add <- info_list$current_pos - 7
  if (pos_to_add < 1) {
    pos_to_add <- length(circle) + pos_to_add
  }
  value  <- circle[pos_to_add] + i
  circle <- circle[-pos_to_add]
  if (pos_to_add > length(circle)) {
    current_post <- 1
  } else {
    current_pos <- pos_to_add
  }
  list(circle = circle, current_pos = current_pos, value = value)
}

play_game <- function(nr_players,
                      nr_marbles) {
  info_list <- list(circle = c(0, 1), current_pos = 2)
  score_vec <- rep(0, nr_players)
  for (i in 2:nr_marbles) {
    if (i %% 23 != 0) {
      info_list <- add_marble(info_list, i)
    } else {
      info_value_list <- get_score(i, info_list)
      info_list <- info_value_list[1:2]
      player_active <- i %% nr_players
      if (player_active == 0) player_active <- nr_players
      score_vec[player_active] <-  score_vec[player_active] + 
        info_value_list$value
    }
   if (i %% 5000 == 0) print(i) 
  }
  score_vec
}

play_game(470, 72170) %>% 

# Part 2
play_game(470, 72170 * 100) %>% max()
