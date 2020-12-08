library(tidyverse)
d8 <- read_csv("data/data08", col_names = FALSE) %>% 
  extract(X1, c("act", "val"), "(.*) (.*)") %>% 
  mutate(val = as.numeric(val))

# star 1
i <- 1; acc <- 0; visited <- i
while (length(visited) == length(unique(visited))) {
  iter <- d8[i, ]
  if (iter$act == "acc") {acc <- acc + iter$val; i <- i + 1}
  else if (iter$act == "jmp") {i <- i + iter$val}
  else {i <- i + 1}
  visited <- c(visited, i)
}

# star 2
see_if_it_runs <- function(x) {
  i <- 1; acc <- 0; visited <- i
  while (length(visited) == c(length(unique(visited)))) {
    iter <- x[i, ]
    if (iter$act == "acc") {acc <- acc + iter$val; i <- i + 1}
    else if (iter$act == "jmp") {i <- i + iter$val}
    else {i <- i + 1}
    visited <- c(visited, i)
    if (i > nrow(x)) {
      print(paste0("Program completed, value: ", acc))
      return(TRUE)
    }
  }
  return(FALSE)
}

change_rows <- which(d8$act %in% c("jmp", "nop"))
for (i in change_rows) {
  x <- d8
  x[i, ]$act <- ifelse(x[i, ]$act == "jmp", "nop", "jmp")
  if (see_if_it_runs(x) ) break
}
