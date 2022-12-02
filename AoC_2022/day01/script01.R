library(tidyverse)
ints <- as.numeric(readLines("data01.txt"))

cals <- tibble(ints = ints) |> 
  mutate(elve = cumsum(is.na(ints))) |> 
  group_by(elve) |> 
  summarise(tot = sum(ints, na.rm = TRUE)) |> 
  arrange(desc(tot)) |> 
  pull()

paste("Star 1 =", cals[1])
paste("Star 2 =", sum(cals[1:3]))
