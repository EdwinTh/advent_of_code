library(tidyverse)
d19 <- read_lines("data/data19")

# star 1
rls <- d19[1:(which(d19 == "") - 1)]
rls_nr <- str_split(rls, ": ") %>% map_chr(1)
rls    <- str_split(rls, ": ") %>% map_chr(2) %>% str_replace_all('\\\"', "") %>% 
  str_split(" \\| ")
names(rls) <- rls_nr
msg <- d19[(which(d19 == "") + 1):length(d19)]

get_ab <- function(rl = "0") {
  r <- rls[[rl]]
  if (r[1] %in% c("a", "b")) return(r)
  spl <- str_split(r, " ")
  if (length(spl) == 1) {
    map(spl[[1]], get_ab)
  } else {
    c(map(spl[[1]], get_ab), 
      map(spl[[2]], get_ab))
  }
}
tree <- get_ab("0")

resolve_tree <- function(tree_el) {
  if (length(tree_el) == 1) return(tree_el)
  c(map(tree_el[1:2], resolve_tree), map(tree_el[3:4], resolve_tree))
}

