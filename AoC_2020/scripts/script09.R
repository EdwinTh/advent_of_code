library(tidyverse)
d9 <- read_lines("data/data09") %>% as.numeric()

# star 1
i <- 26 
while (d9[i] %in% apply(combn(d9[(i-25):(i-1)], 2), 2, sum)) i <- i + 1
(star1 <- d9[i])

# star 2
check_iter <- function(i) {
  x <- d9[i:length(d9)]
  if (star1 %in% cumsum(x)) {
    return(x[1:(which(cumsum(x) == star1))])
  }
  check_iter(i + 1)
}
check_iter(1) %>% range() %>% sum()