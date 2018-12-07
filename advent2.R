# Part 1
library(stringr)
ids <- readLines('~/Desktop/advent_data2')
all_counts <- ids %>%
  str_split("") %>%
  map(table)

# 3 is max nr of repetitions, so only check for 2 and 3
unlist(all_counts) %>% max()

has2 <- map_lgl(all_counts, ~2 %in% .x)
has3 <- map_lgl(all_counts, ~3 %in% .x)
sum(has2) * sum(has3)

# Part 2
all_splitted <- ids %>% str_split("")
n <- length(ids)

inds <- combn(1:n, 2) %>%
  t() %>%
  as_data_frame()

get_dif <- function(letters1, letters2) {
  sum(letters1 != letters2)
}

difs <- map2_int(inds$V1,
                 inds$V2,
                 ~get_dif(all_splitted[[.x]], all_splited[[.y]]))
the_two <- all_splitted[inds[which(difs == 1), ] %>% unlist]

the_two[[1]][the_two[[1]] == the_two[[2]]] %>%
  paste0(collapse = "")
