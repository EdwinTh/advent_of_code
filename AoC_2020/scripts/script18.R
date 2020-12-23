library(tidyverse); options(scipen = 999)
d18 <- read_lines("data/data18")

# star 1
d18_spl <- str_split(d18, "") %>% map(~.x[.x != " "])

resolve_element <- function(el) {
  nrs <- as.numeric(str_extract_all(el, "\\d+")) %>% .[!is.na(.)]
  ops <- str_extract_all(el, "\\+|\\*") %>% unlist()
  ret <- nrs[1]
  nrs <- nrs[-1]
  for (i in seq_along(nrs)) {
    ret <- ifelse(ops[i] == "+", ret + nrs[i], ret * nrs[i])
  }
  ret
}

resolve_deepest_level <- function(x, fun = resolve_element) {
  lvl        <- cumsum(as.numeric(x == "(") - as.numeric(x == ")"))
  to_resolve <- which(lvl == max(lvl))
  el_index   <- split(to_resolve, cumsum(c(FALSE, diff(to_resolve) > 1))) %>% 
    map(~c(.x, max(.x) + 1))
  vals       <- map_dbl(el_index, ~fun(x[.x][-c(1, length(.x))]))
  non_el_index <- setdiff(1:length(x), unlist(el_index))
  non_el     <- split(x[non_el_index], cumsum(c(FALSE, diff(non_el_index) > 1)))
  ret        <- vector("list", length(vals) + length(non_el))
  val_first  <- 1 %in% unlist(el_index)
  for (i in seq_along(ret)) {
    if (val_first) {
      if ( i %% 2 == 1) {ret[[i]] <- vals[[1]];   vals   <- vals[-1]}
      else              {ret[[i]] <- non_el[[1]]; non_el <- non_el[-1]}
    } else {
      if ( i %% 2 == 1) {ret[[i]] <- non_el[[1]]; non_el <- non_el[-1]}
      else              {ret[[i]] <- vals[[1]];   vals   <- vals[-1]}
    } 
  }
  unlist(ret)
}

resolve <- function(x, fun) {
  if (! "(" %in% x) return(fun(x))
  resolve(resolve_deepest_level(x, fun), fun)
}
map_dbl(d18_spl, ~resolve(.x, fun = resolve_element)) %>% sum()

# star 2
resolve_element2 <- function(el) {
  nrs <- as.numeric(str_extract_all(el, "\\d+")) %>% .[!is.na(.)]
  ops <- str_extract_all(el, "\\+|\\*") %>% unlist()
  plusses <- which(ops == "+")
  os <- 0
  for (i in plusses) {
    nrs[i - os] <- nrs[i - os] + nrs[i + 1 - os]
    nrs <- nrs[-(i + 1 -os)]
    os <- os + 1
  }
  prod(nrs)
}
map_dbl(d18_spl, ~resolve(.x, fun = resolve_element2)) %>% sum()
