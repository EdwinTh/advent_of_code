library(tidyverse)
library(stringr)

## Part 1
adv5 <- readLines("data/advent_data5")
all_letters <- adv5 %>% str_split("") %>% unlist()

get_pop_ind <- function(x) {
  n <- length(x)
  z <- x[1:(n - 1)]
  y <- x[2:n]
  tolower(z) == tolower(y) & z != y
} 

pop_first_match <- function(x,
                            pop_ind) {
  first_pop <- pop_ind %>% which() %>% min()
  x[-c(first_pop, first_pop + 1)]
}

remaining_letters <- all_letters
pop_ind <- get_pop_ind(all_letters)

while (any(pop_ind)) {
  remaining_letters <- pop_first_match(remaining_letters,
                                       pop_ind) 
  pop_ind <- get_pop_ind(remaining_letters)
  print(length(remaining_letters))
}

length(remaining_letters)

# this is of course not where R shines, takes a few mins. 
# Unfortunately a vectorised implementation is dificult
# because of the sequences like aAa

## Part 2
# Ha, now we need to do it 26 times. We have to vectorise here somehow.

pop_all_following <- function(all_letters) {
  comb_id <- 1:(length(all_letters) - 1)
  ind_df  <- data_frame(comb_id    = comb_id, 
                        first_ind  = comb_id,
                        second_ind = comb_id + 1)
  to_pop <- ind_df[all_letters %>% get_pop_ind(), ] %>% 
    gather(key = order, value = ind, -comb_id)
  
  double_comb <- 
    to_pop %>% count(ind) %>% 
    filter(n > 1) 
  
  combs_to_pop <- to_pop %>% 
    filter(order == "first_ind") %>% 
    anti_join(double_comb, by = "ind") %>% 
    select(comb_id)
  
  inds <- to_pop %>% inner_join(combs_to_pop, by = "comb_id")  %>% 
    pull(ind)
  
  all_letters[!1:length(all_letters) %in% inds]
}

got_to_pop_them_all <- function(remaining_letters) {
  while( any(get_pop_ind(remaining_letters)) ) {
    remaining_letters <- pop_all_following(remaining_letters)
  }
  remaining_letters
}

letters_removed <- map(letters, 
                       ~all_letters[tolower(all_letters) != .x])

library(furrr)
plan(multiprocess)
fully_popped <- furrr::future_map(letters_removed, 
                                  ~got_to_pop_them_all(.x) %>% length())
