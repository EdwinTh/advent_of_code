library(tidyverse)
d23 <- "219347865" %>% str_split("") %>% unlist() %>% as.numeric()

# star 1
find_next_val <- function(cv, nonsel, mv) {
  cv_1 <- ifelse(cv == 1, mv, cv - 1)
  if (cv_1 %in% nonsel) return(cv_1)
  find_next_val(cv_1, nonsel, mv)
}

play_round <- function(x, cp = 1, mv = 9) {
  cv       <- x[cp]
  sel_ind  <- ifelse(cp + 1:3 > mv, abs(cp + 1:3 - mv), cp + 1:3)
  selected <- x[sel_ind]
  nonsel   <- x[-sel_ind]
  next_val <- find_next_val(cv, nonsel, mv)
  ret_x    <- append(nonsel, selected, which(nonsel == next_val))
  cp       <- which(cv == ret_x) + 1
  list(x = ret_x, cp = ifelse(cp == (mv + 1), 1, cp))
}

play_n_rounds <- function(x, n) {
  cp <- 1
  mv <- max(x)
  for(i in 1:n) {
    rnd <- play_round(x, cp, mv)
    x  <- rnd$x
    cp <- rnd$cp
  }
  x
}

r100 <- play_n_rounds(d23, 100)
paste(r100[c(9, 1:7)], collapse ="")

# star 2
profvis(play_n_rounds(c(d23, 10:1e6), 10))
