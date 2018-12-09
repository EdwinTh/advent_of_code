library(stringr)
library(tidyverse)

## Part 1
adv7 <- readLines("data/advent_data7")
adv7_df <- data_frame(
  first = adv7 %>% str_extract_all("[A-Z]") %>% map_chr(2),
  after = adv7 %>% str_extract_all("[A-Z]") %>% map_chr(3)
)

impeded_df <- adv7_df %>% tidyr::nest(-after)

remove_done_impediments <- function(df, letter = "E") {
  df %>% 
    mutate(data = map(data, ~.x %>% filter(first != letter)))
}

find_freed_up_steps <- function(df) {
  df %>% 
    filter(map_lgl(data, ~nrow(.x) == 0)) %>% 
    pull(after)
}

remove_freed_up_steps <- function(df) {
  df %>% 
    filter(map_lgl(data, ~nrow(.x) != 0)) 
}

done_steps <- character()
available <- adv7_df$first[!adv7_df$first %in% adv7_df$after] %>% 
  unique()

while (nrow(impeded_df) > 0) {
  step_this_iteration <- sort(available)[1]
  done_steps <- c(done_steps, step_this_iteration)
  available  <- available[available != step_this_iteration] 
  impeded_df <- remove_done_impediments(impeded_df, step_this_iteration)
  available  <- c(available, find_freed_up_steps(impeded_df))
  impeded_df <- remove_freed_up_steps(impeded_df)
}
c(done_steps, available) %>% paste(collapse = "")

## Part 2
update_tasks <- function(tasks, 
                         letter, 
                         row_nr) {
  first_free <- which(tasks[row_nr, ] == "") %>% min()
  if (length(first_free) == 0) return(tasks)
  step_time  <- (1:26)[LETTERS == letter] + 60
  tasks[row_nr:(row_nr + step_time), first_free] <- letter
  tasks
}

check_done_steps <- function(tasks, 
                             row_nr) {
  steps_this_sec <- tasks[row_nr, ] %>% unlist()
  steps_next_sec <- tasks[row_nr + 1, ] %>% unlist()
  done_steps <- setdiff(steps_this_sec, steps_next_sec)
  done_steps[done_steps != ""]
}

done_steps <- character()
available <- adv7_df$first[!adv7_df$first %in% adv7_df$after] %>% 
  unique()

impeded_df <- adv7_df %>% tidyr::nest(-after)

max_seconds <- 26 * 60 + sum(1:26)
worker_df <- data_frame(worker = character(max_seconds))
tasks <- 
  bind_cols(worker_df, worker_df, worker_df, worker_df, worker_df)

for (i in 1:max_seconds) {
  
  ## assign pending steps to worker
  if (length(available) > 0) {
    for (step in sort(available)) {
      tasks <- update_tasks(tasks, step, i)
      available <- available[available != step]
    }
  }
  
  ## bookkeeping on steps like in Task 1
  done_steps_this_iter <- check_done_steps(tasks, i)
  if (length(done_steps_this_iter) > 0) {
    done_steps <- c(done_steps, done_steps_this_iter)
    for (step in done_steps_this_iter) {
      impeded_df <- remove_done_impediments(impeded_df, step) 
    }
    available  <- c(available, find_freed_up_steps(impeded_df))
    impeded_df <- remove_freed_up_steps(impeded_df)
  }
}  
  