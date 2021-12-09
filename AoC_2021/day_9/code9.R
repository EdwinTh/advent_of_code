library(tidyverse)
splitted <- readLines('day_9/data9.txt') |> strsplit("") 
nrs <- unlist(splitted) |> as.integer() 

# star 1
coords <- tibble(val = nrs, 
                 ri  = rep(1:length(splitted), each = length(splitted[[1]])),
                 ci  = rep(1:length(splitted[[1]]), length(splitted)))
with_adj <- 
  sqldf::sqldf("select c.*, ca.ri as ri_a, ca.ci as ci_a, ca.val as val_a
                from coords as c
                inner join coords as ca
                on ca.ri >= (c.ri - 1) and ca.ri <= (c.ri + 1)
                and ca.ci >= (c.ci - 1) and ca.ci <= (c.ci + 1)") |>
  as_tibble() |> 
  filter(!(ri == ri_a & ci == ci_a), ri == ri_a | ci == ci_a)
  
local_mins <- with_adj |> 
  group_by(ci, ri) |>
  filter(all(val < val_a) | val == 0) |>
  ungroup() |>
  select(val, ci, ri) |>
  distinct()
sum(local_mins$val + 1)

# star 2
adj_none_9 <- function(rw, cl, with_adj) {
  with_adj |> filter(ri == rw, ci == cl, val_a < 9) |>
    select(ri_a, ci_a)
}

df_to_list <- function(df) {
  map(split(df, rownames(df)), unlist)
}

select_new_inds <- function(new_inds, in_basin) {
  ni <- map_chr(new_inds, ~paste(.x, collapse =  "-"))
  ib <- map_chr(in_basin, ~paste(.x, collapse =  "-"))
  new_inds[!ni %in% ib]
}

find_basin_size <- function(rw, cl) {
  to_run <- in_basin <- list(c(rw, cl))
  while(length(to_run) > 0) {
    new_inds <- adj_none_9(to_run[[1]][1], to_run[[1]][2], with_adj) |>
      df_to_list() |> select_new_inds(in_basin)
    in_basin <- c(in_basin, new_inds)
    to_run <- c(to_run[-1], new_inds)
  }
  length(in_basin)
}

map2_int(local_mins$ri, local_mins$ci, find_basin_size) |> sort() |> rev() %>% 
  `[`(1:3) |> prod()
