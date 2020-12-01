library(tidyverse)
library(stringr)

## Part 1
adv4 <- readLines("data/advent_data4") %>% 
  sort()
splitted <- adv4 %>% 
  str_remove("\\[") %>% 
  str_split("\\] ")

adv4_df <- data_frame(
  tm    = map_chr(splitted, 1),
  info  = map_chr(splitted, 2)) %>% 
  mutate(day = str_sub(tm, 1, 10) %>% as.Date,
         hm  = str_sub(tm, 12, 16))

guard_info <- adv4_df %>% 
  filter(str_sub(info, 1, 1) == "G") %>% 
  mutate(id = str_extract(info, "\\d+")) %>% 
  select(-info) %>% 
  mutate(shift_day = ifelse(str_sub(hm, 1, 1) == "2",
                            day + 1,
                            day) %>% as.Date(origin = "1970-01-01")) %>% 
  select(id, shift_day)

wake_info <- adv4_df %>% 
  filter(str_sub(info, 1, 1) != "G") 

# check if all are after midnight
wake_info$hm %>% str_sub(1, 1) %>% table()

full_info <- 
  inner_join(guard_info, wake_info, by = c("shift_day" = "day")) %>% 
  select(id, info, hm) %>% 
  mutate(min_nmrc = str_replace(hm, ":", "") %>% as.numeric()) 

uneven <- (1:nrow(full_info)) %% 2 %>% `==`(1)

full_info[uneven, ] %>% distinct(info)
full_info[!uneven, ] %>% distinct(info)

sleep_wake_df <- 
  full_info[uneven, ] %>% 
  select(id, sleep = min_nmrc) %>% 
  bind_cols(full_info[!uneven, ] %>% 
              select(wake = min_nmrc))

sleepy_guard_id <- sleep_wake_df %>% 
  mutate(mins_asleep = map2_dbl(sleep, wake, ~length(.x:(.y-1)) )) %>% 
  group_by(id) %>% 
  summarise(total_asleep = sum(mins_asleep)) %>% 
  arrange(total_asleep) %>% 
  tail(1) %>% 
  pull(id)

min_most_asleep <- sleep_wake_df %>% 
  filter(id == sleepy_guard_id) %>% 
  mutate(mins_asleep = map2(sleep, wake, ~.x:(.y-1))) %>% 
  pull(mins_asleep) %>% 
  unlist() %>% 
  table() %>% 
  sort() %>% 
  tail(1) %>% 
  names()

as.numeric(sleepy_guard_id) * as.numeric(min_most_asleep)

## Part 2
minute_slept_most <- sleep_wake_df %>% 
  mutate(minute = map2(sleep, wake, ~.x:(.y-1))) %>% 
  select(-sleep, - wake) %>% 
  tidyr::unnest() %>% 
  count(id, minute) %>% 
  filter(n == max(n))

as.numeric(minute_slept_most$id) * minute_slept_most$minute
