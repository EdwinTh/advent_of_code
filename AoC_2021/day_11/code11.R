library(tidyverse)
splitted <- readLines('day_11/data.txt') |> strsplit("") 
nrs <- unlist(splitted) |> as.integer() 

# star 1
coords <- tibble(val = nrs, 
                 ri  = rep(1:length(splitted), each = length(splitted[[1]])),
                 ci  = rep(1:length(splitted[[1]]), length(splitted)))
adjacent_mapping <- 
  sqldf::sqldf("select c.*, ca.ri as ri_a, ca.ci as ci_a, ca.val as val_a
                from coords as c
                inner join coords as ca
                on ca.ri >= (c.ri - 1) and ca.ri <= (c.ri + 1)
                and ca.ci >= (c.ci - 1) and ca.ci <= (c.ci + 1)") |>
  as_tibble() |> 
  filter(!(ri == ri_a & ci == ci_a)) |>
  select(ri, ci, ri_a, ci_a)

take_step <- function(crd, am) {
  new_crd <- crd |> mutate(val = val + 1) |> mutate(flashed = FALSE)
  upd_adj(new_crd, am)
}

upd_adj <- function(new_crd, am) {
  will_flash <- new_crd |> filter(val > 9 & !flashed)
  if (nrow(will_flash) == 0) {
    new_crd <- new_crd |> mutate(val = if_else(flashed, 0, val))
    return(new_crd)
  } 
  new_crd <- new_crd |> mutate(flashed = if_else(val > 9 & !flashed, TRUE, flashed))
  flash_adj <- inner_join(will_flash, am) |> count(ri_a, ci_a)
  new_crd <- left_join(new_crd, flash_adj, by = c('ri' = 'ri_a', 'ci' = 'ci_a')) |>
    mutate(val = val + coalesce(n, 0))
  upd_adj(new_crd |> select(-n), am)
}

flashes <- 0
for (i in 1:100) {
  coords <- take_step(coords, adjacent_mapping)
  flashes <- flashes + sum(coords$flashed)
  coords <- coords |> select(-flashed)
}
print(flashes)

# star 2 - assuming it did not occur in the first 100 ;)
coords <- tibble(val = nrs, 
                 ri  = rep(1:length(splitted), each = length(splitted[[1]])),
                 ci  = rep(1:length(splitted[[1]]), length(splitted)))
iter <- 0
while (TRUE) {
  iter = iter + 1
  coords <- take_step(coords, adjacent_mapping)
  if (sum(coords$flashed) == 100) {
    print(iter)
    break
  }
  coords <- coords |> select(-flashed)
}

