library(tidyverse)
# star 1
splitted <- readLines('day_15/test_data.txt') %>% strsplit("") 
nrs <- unlist(splitted) %>% as.integer() 
coords <- tibble(val = nrs, 
                 ri  = rep(1:length(splitted), each = length(splitted[[1]])),
                 ci  = rep(1:length(splitted[[1]]), length(splitted))) %>% 
  mutate(distance = c(0, rep(Inf, nrow(.)-1)))

adjacent_mapping <- 
  sqldf::sqldf("select c.*, ca.ri as ri_a, ca.ci as ci_a, ca.val as val_a
                from coords as c
                inner join coords as ca
                on ca.ri >= (c.ri - 1) and ca.ri <= (c.ri + 1)
                and ca.ci >= (c.ci - 1) and ca.ci <= (c.ci + 1)") %>% 
  as_tibble() %>% 
  filter(!(ri == ri_a & ci == ci_a), ri == ri_a | ci == ci_a) %>% 
  select(ri, ci, ri_a, ci_a)

dijkstra <- function(crd, am) {
  pos <- crd %>% filter(distance == min(distance))
  am_with_val <- inner_join(am, crd %>% select(ri_a = ri, ci_a = ci, val), by = c("ri_a", "ci_a"))
  updated <- inner_join(pos %>% select(-val), am_with_val, by = c("ri", "ci")) %>% 
    mutate(distance_new = distance + val) %>% 
    select(ri = ri_a, ci = ci_a, distance_new) %>% 
    group_by(ri, ci) %>% 
    summarise(distance_new = min(distance_new), .groups = 'drop')
  crd_new <- left_join(crd, updated, by = c("ri", "ci")) %>% 
    mutate(distance_new = coalesce(distance_new, Inf)
           ,distance = pmin(distance, distance_new)) %>% 
    select(-distance_new)
  
  if (any((pos$ri == max(crd$ri)) & pos$ci == max(crd$ci)) ) {
    return(crd_new %>% filter(ri == max(ri) & ci == max(ci)) %>% pull(distance))
  }
  
  print(pos[1, ])
  
  crd <- crd_new %>% anti_join(pos %>% select(ri, ci), by = c("ri", "ci"))
  am <- am %>% anti_join(pos %>% select(ri, ci), by = c("ri", "ci"))
  dijkstra(crd, am)
}

system.time(dijkstra(coords, adjacent_mapping))

# star 2
splitted <- readLines('day_15/data.txt') %>% strsplit("") %>% map(as.integer)
re <- map(splitted, function(x) {
  nrs <- c(x, x+1, x+2, x+3, x+4)
  ifelse(nrs < 10, nrs, nrs - 9)
})

splitted <- c(re, map(re, ~.x+1), map(re, ~.x+2), map(re, ~.x+3), map(re, ~.x+4)) %>% 
  map(~ifelse(.x < 10, .x, .x - 9))
nrs <- unlist(splitted) %>% as.integer() 

coords <- tibble(val = nrs, 
                 ri  = rep(1:length(splitted), each = length(splitted[[1]])),
                 ci  = rep(1:length(splitted[[1]]), length(splitted))) %>% 
  mutate(distance = c(0, rep(Inf, nrow(.)-1)))

all_adjacent <- function(ri = 1, ci = 1, max_val) {
  expand_grid(ri_a = (ri-1):(ri+1), ci_a = (ci-1):(ci+1)) %>% 
  mutate(ri = ri, ci = ci) %>%   
  filter(!(ri == ri_a & ci == ci_a)
         ,ri == ri_a | ci == ci_a
         ,ri_a > 0, ci_a > 0, ri_a <= max_val, ci_a <= max_val) %>% 
  select(ri, ci, ri_a, ci_a)
}

adjacent_mapping <- map2_dfr(coords$ci, coords$ri, all_adjacent, max_val = length(splitted))

dijkstra_step <- function(crd, am) {
  pos <- crd %>% filter(distance == min(distance))
  am_with_val <- inner_join(am, crd %>% select(ri_a = ri, ci_a = ci, val), by = c("ri_a", "ci_a"))
  updated <- inner_join(pos %>% select(-val), am_with_val, by = c("ri", "ci")) %>% 
    mutate(distance_new = distance + val) %>% 
    select(ri = ri_a, ci = ci_a, distance_new) %>% 
    group_by(ri, ci) %>% 
    summarise(distance_new = min(distance_new), .groups = 'drop')
  crd_new <- left_join(crd, updated, by = c("ri", "ci")) %>% 
    mutate(distance_new = coalesce(distance_new, Inf)
           ,distance = pmin(distance, distance_new)) %>% 
    select(-distance_new)
  
  print(pos[1, ])
  
  if (any((pos$ri == max(crd$ri)) & pos$ci == max(crd$ci)) ) {
    print(crd_new %>% filter(ri == max(crd$ri)) & pos$ci == max(crd$ci))
    break
  }
  
  crd <- crd_new %>% anti_join(pos %>% select(ri, ci), by = c("ri", "ci"))
  am <- am %>% anti_join(pos %>% select(ri, ci), by = c("ri", "ci"))
  return(list(crd, am))
}
step_res <- dijkstra_step(coords, adjacent_mapping)
while (TRUE){
  step_res <- dijkstra_step(step_res[[1]], step_res[[2]])
}

