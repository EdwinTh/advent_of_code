library(tidyverse)
d13 <- readLines("~/Desktop/data13")

clean_line <- function(l) {
  spl <- str_split(l, " ")[[1]]
# star1
  tibble(from  = spl[1], 
         to    = str_split(spl[11], "\\.")[[1]][1],
         value = ifelse(spl[[3]] == "lose", -1, 1) * as.numeric(spl[4])) 
}

d13 <- map_dfr(d13, clean_line)
p   <- unique(d13$from)

make_pairs <- function(arr, nr) {
  ret <- tibble(s1 = rep("a", length(arr)), s2 = rep("a", length(arr)), nr = nr)
  for (i in seq_along(arr)) {
    i2 <- ifelse(i == length(arr), 1, i + 1)
    ret[i,1] <- arr[i]
    ret[i,2] <- arr[i2]
  }
  ret
}

all_combs <- gtools::permutations(n = length(p), r = length(p), v = p) %>% 
  apply(1, as.list) %>% 
  map(unlist)

map2_dfr(all_combs, seq_along(all_combs), make_pairs) %>% 
  inner_join(d13, by = c("s1" = "from", "s2" = "to")) %>% 
  inner_join(d13, by = c("s1" = "to", "s2" = "from")) %>% 
  pivot_longer(cols = starts_with("val")) %>% 
  group_by(nr) %>% 
  summarise(tot = sum(value)) %>% 
  arrange(desc(tot))
  
# star 2
me_df <- tibble(from  = c(rep("me", 8), unique(d13$from)),
                to    = c(unique(d13$from), c(rep("me", 8))),
                value = 0)
d13_2 <- bind_rows(d13, me_df)
p2    <- unique(d13_2$from)

all_combs2 <- gtools::permutations(n = length(p2), r = length(p2), v = p2) %>% 
  apply(1, as.list) %>% 
  map(unlist)

map2_dfr(all_combs2[1:45360], 1:45360, make_pairs) %>% 
  inner_join(d13, by = c("s1" = "from", "s2" = "to")) %>% 
  inner_join(d13, by = c("s1" = "to", "s2" = "from")) %>% 
  pivot_longer(cols = starts_with("val")) %>% 
  group_by(nr) %>% 
  summarise(tot = sum(value)) %>% 
  arrange(desc(tot))
