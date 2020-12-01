library(tidyverse)
library(stringr)

## part 1
a <- readLines("data/advent_data8") %>% 
  str_split(" ") %>% unlist() %>% as.numeric()
df <- data_frame(id     = 1, 
                 parent = NA, 
                 children  = list(NULL), 
                 meta_length = NA, 
                 meta        = NA)

add_new_nodes <- function(df, current_id, children, meta_length, last_id) {
  child_ids <- (last_id + 1):(last_id + children)
  new_rows <- data_frame(id = child_ids, parent = current_id, children = NA, meta_length = NA, meta = NA)
  df[df$id == current_id, ]$children <- list(child_ids)
  bind_rows(df, new_rows)
}

add_meta <- function(df, current_id, meta_length, meta_vec) {
  df[df$id == current_id, ]$meta_length <- meta_length
  df[df$id == current_id, ]$meta        <- list(meta_vec)
  df
}

update_current_id <- function(df, current_id) {
  
  current_row <- df %>% filter(id == current_id)
  children <- current_row$children[[1]]
  
  if (children[1] == 0) {
    
    return(current_row$parent)
    
  } else {
    
    has_no_meta <- check_children(children) 
    
    if (any(has_no_meta)) {
      
      return(children[has_no_meta][1])
      
    } else {
      
      return(current_row$parent)
    }
  }
}

check_children <- function(children) {
  map_lgl(children, 
          ~df %>% 
            filter(id == .x) %>% 
            pull(meta) %>%
            unlist %>% 
            is.na %>% 
            all)
}

current_id <- 1
last_id    <- 1

while(length(a) > 0) {
  current_row <- filter(df, id == current_id)
  last_id     <- df$id %>% max()
  current_children <- current_row$children[[1]]
  if (is.null(current_children) & a[1] > 0) {
    df <- add_new_nodes(df, current_id, a[1], a[2], last_id)
    df[df$id == current_id, ]$meta_length <- a[2]
    a  <- a[-c(1, 2)]
  } else if (is.null(current_children)) {
    df <- add_meta(df, current_id, a[2], a[3:(3 + a[2] - 1)])
    df[df$id == current_id, ]$children <- 0
    a <- a[-c(1:(a[2]  + 2))]
  } else {
    children_left <- check_children(current_children) %>% any()
    if (!children_left) {
      ml <- current_row$meta_length
      df <- add_meta(df, current_id, ml, a[1:ml])
      a <- a[-c(1:ml)]
    }
  }
  current_id <- update_current_id(df, current_id)
}

## part 2
df_part2 <- df %>% 
  mutate(is_end_node = map_lgl(children, ~.x[1] == 0),
         value       = map_dbl(meta, sum))

to_check <- 1
values   <- numeric(0)

while(length(to_check) > 0) {
  current_row <- filter(df_part2, id == to_check[1])
  if (current_row$is_end_node) {
    values <- c(values, current_row$value)
    to_check <- to_check[-1]
  } else {
    id_to_add <- unlist(current_row$children)[unlist(current_row$meta)]
    id_to_add <- id_to_add[!is.na(id_to_add)]
    to_check <- c(to_check[-1], id_to_add)
  }
}
sum(values)
  
