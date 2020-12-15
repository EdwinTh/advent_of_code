library(tidyverse)
d15 <- c(15,5,1,4,7,0)

# star 1 
l <- length(d15)

while(l < 2021) {
  last <- d15[l]
  d15 <- c(d15, ifelse(last %in% d15[-l], 
                       l - max(which(d15[-l] == last)),
                       0))
  l <- l + 1
}
last

# star 2
d15 <-  c(15,5,1,4,7,0)
mem <- numeric(3 * 10^7)

for (i in seq_along(d15)) {
  mem[d152[i] + 1] <- i
}

cur_val <- 0
i <- length(d15) + 1
max_i <- 3*10^7
while (i <= max_i){
  if (i == (max_i)) print(cur_val)
  if (!mem[cur_val + 1]) {
    mem[cur_val + 1] <- i
    cur_val <- 0
  } else {
    next_cur_val <- i - mem[cur_val + 1]
    mem[cur_val+1] <- i
    cur_val <- next_cur_val
  }
  i <- i + 1
}

