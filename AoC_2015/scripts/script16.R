library(tidyverse)
d16 <- readLines("/data/data16")

# star 1
d16_cl <- map(str_split(d16, " "), ~.x %>% str_replace_all(",|:", "") %>% `[`(3:8)) %>% 
  map(function(x) {
    ret <- as.numeric(x[c(2, 4, 6)])
    names(ret) <- x[c(1, 3, 5)]
    ret
    })

the_Sue <- c("children" = 3, "cats" = 7, "samoyeds" = 2, "pomeranians" = 3,
             "akitas" = 0, "vizslas" = 0, "goldfish" = 5, "trees" = 3, "cars" = 2,
             "perfumes" = 1)

map_lgl(d16_cl, ~all(the_Sue[names(.x)] == .x)) %>% which()

# star 2
greater_vars <- c("cats", "trees")
smaller_vars <- c("pomeranians", "goldfish")
equal_vars   <- setdiff(names(the_Sue), c(greater_vars, smaller_vars))
is_the_sue <- function(x) {
  the_Sue_sel <- the_Sue[names(x)]
  ret <- c(x[greater_vars] > the_Sue_sel[greater_vars],
    x[smaller_vars] < the_Sue_sel[smaller_vars],
    x[equal_vars] == the_Sue_sel[equal_vars])
  all(ret[!is.na(ret)])
}

map_lgl(d16_cl, is_the_sue) %>% which

