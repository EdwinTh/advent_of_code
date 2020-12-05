library(tidyverse)
d4 <- readLines("data/data04")

documents <- split(d4, cumsum(rep(0, length(d4)) + (d4 == ""))) %>% 
  map_chr(~paste(.x, collapse = " ") %>% str_trim) 

into_key_value <- function(x) {
  values <- map_chr(str_split(x, ":"), 2)
  names(values) <- map_chr(str_split(x, ":"), 1)
  values
}

kv <- map(str_split(documents, " "), into_key_value)

# star 1
sum(map_dbl(kv, ~names(.x) %>% .[. != "cid"] %>% length()) == 7)

# star 2
kv <- kv[map_dbl(kv, ~names(.x) %>% .[. != "cid"] %>% length()) == 7]
betw <- function(x, a, b) x >= a & x <= b

test_hgt <- function(x) {
  nr <- as.numeric(str_extract(x, "\\d+"))
  if (str_detect(x, "cm")) betw(nr, 150, 193)
  else if (str_detect(x, "in")) betw(nr, 59, 76)
  else FALSE
}

test_hcl <- function(x) {
  xs <- str_split(x, "")[[1]]
  length(xs) == 7 & xs[1] == "#" & all(xs[2:7] %in% c(0:9, letters[1:6]))
}

test_pid <- function(x) {
  xs <- str_split(x, "")[[1]]
  length(xs) == 9 & all(xs %in% 0:9)
}

valid2 <- map_lgl(kv, ~betw(as.numeric(.x["byr"]), 1920, 2002)) &
  map_lgl(kv, ~betw(as.numeric(.x["iyr"]), 2010, 2020)) &
  map_lgl(kv, ~betw(as.numeric(.x["eyr"]), 2020, 2030)) &
  map_lgl(kv, ~test_hgt(.x["hgt"])) &
  map_lgl(kv, ~test_hcl(.x["hcl"])) &
  map_lgl(kv, ~.x["ecl"] %in% c("amb", "blu", "brn", "gry", "grn", "hzl", "oth")) &
  map_lgl(kv, ~test_pid(.x["pid"]))

sum(valid2)
  