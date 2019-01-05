library(tidyverse)

initial_state <- readLines("data/advent_data_12_1") %>% 
  str_split("") %>% unlist()
names(initial_state) <- 0:(length(initial_state) - 1)

growth <- readLines("data/advent_data_12_2")
growth_df <- growth %>% 
  str_split(" => ") %>% 
  map_dfr(~data_frame(state = .x[1], new = .x[2]))

## Part 1
add_empty_pots <- function(state) {
  pad_before <- rep(".", 3)
  names(pad_before) <- as.numeric(min(names(state) %>% as.numeric)) - 3:1
  pad_after <- rep(".", 4)
  names(pad_after) <- as.numeric(max(names(state) %>% as.numeric)) + 1:4
  c(pad_before, state, pad_after)
} 

get_next_generation <- function(state) {
  pots_with_adjacent <- map_df(names(state) %>% as.numeric, function(ind) {
    all_ind <- (ind - 2):(ind + 2)
    paste0(state[names(state) %in% all_ind], collapse = "") %>% 
      data_frame(ind = ind, this_generation = .)
  }) %>% filter(nchar(this_generation) == 5) 
  
  new_generation <- 
    left_join(pots_with_adjacent, growth_df, by = c("this_generation" = "state")) %>% 
    pull(new)
  new_generation[is.na(new_generation)] <- "."
  names(new_generation) <- pots_with_adjacent$ind
  new_generation
}

generations <- vector("list", 21)
generations[[1]] <- initial_state %>% add_empty_pots()
for (i in 1:20) {
  generations[[i + 1]] <- get_next_generation(generations[[i]]) %>% 
    add_empty_pots()
}

end_state <- generations[[21]]
names(end_state)[end_state == "#"] %>% as.numeric() %>% sum()

## Part 2
init_nr <- initial_state %>% 
  str_replace_all("#" , '2') %>% str_replace_all("\\.", "1") %>% 
  as.numeric() %>% 
  c(1, 1, 1, ., 1, 1)

growth_df_nr <- growth_df %>% 
  mutate(state = str_replace_all(state, "#" , '2') %>% 
           str_split("") %>% 
           map_dbl(~str_replace_all(.x, "\\.", "1") %>% paste0(collapse = "") %>% as.numeric())) %>% 
  mutate(new = str_replace_all(new, "#" , '2') %>% str_replace_all("\\.", "1") %>% as.numeric()) %>% 
  bind_rows(data_frame(state = 0, new = 1))

## TODO beginning and end
state_to_state_df <- function(current_state) {
  data_frame(
    state = c(0, 0, 
              map_dbl(1:(length(current_state) - 4), 
                            ~current_state[.x:(.x + 4)] %>% 
                              paste0(collapse = "") %>% 
                              as.numeric()), 
              0, 0, 0, 0))
}

state <- init_nr
for (i in 1:200) {
  state <- inner_join(
    state_to_state_df(state), growth_df_nr, by = "state"
  ) %>% pull(new)
}

(-3:(length(state)-4))[state == 2]
