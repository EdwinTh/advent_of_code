library(tidyverse)
d22 <- read_lines("data/data22") %>% .[!str_detect(., "P")] %>% as.numeric()
spl <- which(is.na(d22))

# star 1
p1  <- d22[1:(spl-1)]
p2  <- d22[(spl+1):length(d22)]

play_round <- function(p1, p2) {
  nrs <- sort(c(p1[1], p2[1])) %>% rev()
  if (p1[1] > p2[1]) p1 <- c(p1, nrs)
  else p2 <- c(p2, nrs)
  list(p1 = p1[-1], p2 = p2[-1])
}

while ( (length(p1) > 0) & (length(p2) > 0) ) {
  rnd <- play_round(p1, p2)
  p1  <- rnd$p1
  p2  <- rnd$p2
}

if(length(p1) == 0) winner <- p2 else winner <- p1
sum(winner * length(winner):1)

# star 2
p1  <- d22[1:(spl-1)]
p2  <- d22[(spl+1):length(d22)]

collapse_decks <- function(p1, p2) {
  paste(paste(p1, collapse = "-"), paste(p2, collapse ="-"))
}
i = 1

play_game <- function(p1, p2) {
  earlier_decks <- list()
  while ( (length(p1) > 0) & (length(p2) > 0) ) {
    deck <- collapse_decks(p1, p2)
    
    if ( any(map_lgl(earlier_decks, ~.x == deck)) ) {
      return(list(p1 = p1, p2 = p2, winner = "p1"))
      break
    }
    
    p1_draw <- p1[1]; p2_draw <- p2[1]
    
    if (p1_draw < length(p1) & p2_draw < length(p2)) {
      winner <- play_game(p1[-1], p2[-1])$winner
    } else {
      winner <- ifelse(p1_draw > p2_draw, "p1", "p2")
    }
    if (winner == "p1") p1 <- c(p1, p1_draw, p2_draw) else p2 <- c(p2, p2_draw, p1_draw)
    p1 <- p1[-1]; p2 <- p2[-1]
    earlier_decks <- c(earlier_decks, deck)
    print(i)
    i = i +1
  }
  if (length(p1) == 0) winner <- "p2" else winner <- "p2"
  list(p1 = p1, p2 = p2, winner = winner)
}

res <- play_game(p1, p2)
