library(tidyverse); options(scipen=999)
d10 <- read_lines("data/data10") %>% as.numeric() %>% 
  sort() %>% c(0, ., max(.) + 3)

# star 1
table(d10[2:length(d10)] - d10[1:(length(d10)-1)]) %>% prod()

# star 2

# the numbers with three values in between are all fixed, we only consider 
# those with one in between
one_groups <- c(0, cumsum(!d10[1:(length(d10)-1)] + 1 == d10[2:length(d10)]))

# groups of ones with one or two members only have one arrangement and 
# can be ignored
lo <- (split(d10, one_groups) %>% map_dbl(length) %>% table())[3:5]

# groups with 3 members have two arrangements, with 4 4 and with 5 7
# the total nr of possible arrangements is the prod of all arrangements
2^lo['3'] * 4^lo['4'] * 7^lo['5']