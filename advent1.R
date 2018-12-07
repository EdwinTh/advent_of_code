freq_list <- readLines("~/Desktop/tmp.txt") %>%
  stringr::str_replace("\\+", "") %>%
  as.numeric()

# challenge 1
sum(freq_list)

# challenge 2
cumsum(freq_list) %>% table() %>% table()

#trial and error, it is somwhere between 100 and 150 repetitions

## solution 1
for (i in 101:150) {
  cnt <- cumsum(rep(freq_list, i)) %>% table() %>% table()
  if (length(cnt) == 2) {
    break(print(i))
  }
}

up_untill_145 <- cumsum(rep(freq_list, 144))
iter_145 <- freq_list
iter_145[1] <- iter_145[1] + tail(up_untill_145, 1)
inter_145_summed <- cumsum(iter_145)
inter_145_summed[inter_145_summed %in% up_untill_145]

## soluttion2
df <- data_frame(total = rep(freq_list, 200) %>% cumsum()) %>%
  mutate(nr = row_number())

df1 <- df %>% rename(nr_low = nr)
df2 <- df %>% rename(nr_high = nr)
joined <- inner_join(df1, df2, by = "total")
joined %>%
  filter(nr_low != nr_high) %>%
  filter(nr_low < nr_high)  %>%
  filter(nr_high == min(nr_high))
