library(tidyverse)
d19_1 <- readLines("data/data19_1")
d19_2 <- readLines("data/data19_2")

# star 1
mapping <- str_split(d19_1, " => ") %>% 
  map_dfr(~tibble(from = .x[1], to = .x[2]))

spl <- str_split(d19_2, "")[[1]]

check_replacements <- function(pos) {
  ret <- character(0)
  els_at_pos <- c(spl[pos], paste0(spl[pos], spl[pos + 1]))
  if (pos == length(spl)) els_at_pos <- els_at_pos[1]
  one_pos <- mapping %>% filter(from == els_at_pos[1])
  if (nrow(one_pos) > 0) {
    for (i in 1:nrow(one_pos)) {
      spl_new <- spl
      spl_new[pos] <- one_pos$to[i]
      ret <- c(ret, paste(spl_new, collapse = ""))
    }
  }
  
  two_pos <- mapping %>% filter(from == els_at_pos[2])
  if (nrow(two_pos) > 0) {
    for (i in 1:nrow(two_pos)) {
      spl_new <- spl
      spl_new[pos] <- two_pos$to[i]
      ret <- c(ret, paste(spl_new[-(pos+1)], collapse = ""))
    }
  }
  ret
}
map(1:length(spl), check_replacements) %>% 
 unlist() %>% unique() %>% length()

# star 2

