library(tidyverse); options(scipen = 999)
d14 <- read_lines("data/data14") 
d14 <- split(d14, cumsum(str_detect(d14, "mask")))

# star 1
obtain_masked_val <- function(mask, val) {
  val_bits <- c(0, 0, 0, 0, as.numeric(rev(intToBits(val))))
  sum(ifelse(is.na(mask), val_bits,  mask) * c(2^(35:1), 1))
}

mem <- vector("list", 0)
for (i in seq_along(d14)) {
  d14_el <- d14[[i]]
  mask <- str_split(d14_el[[1]], "= ", simplify = TRUE)[2] %>% 
    str_split("") %>% unlist() %>% as.numeric()
  pos_vals <- str_extract_all(d14_el[-1], "\\d+")
  for (j in seq_along(pos_vals)) {
    mem[pos_vals[[j]][1]] <- obtain_masked_val(mask, pos_vals[[j]][2])
  }
}
unlist(mem) %>% sum()

# star 2
obtain_masked_val2 <- function(mask, val) {
  val_bits <- c(0, 0, 0, 0, as.numeric(rev(intToBits(val))))
  ifelse(mask == 1, 1, ifelse(mask == "X", "X", val_bits)) %>% 
    get_all_vals
}

get_all_vals <- function(masked) {
  x_pos    <- which(masked == "X")
  all_opts <- expand.grid(replicate(length(x_pos), list(c(0, 1))))
  ret <- numeric(nrow(all_opts))
  for (k in 1:nrow(all_opts)) {
    m <- masked
    m[x_pos] <- unlist(all_opts[k, ])
    ret[k] <- sum(as.numeric(m) * c(2^(35:1), 1))
  }
  ret
}

mem <- vector("list", 0)
for (i in seq_along(d14)) {
  d14_el <- d14[[i]]
  mask <- str_split(d14_el[[1]], "= ", simplify = TRUE)[2] %>% 
    str_split("") %>% unlist() 
  pos_vals <- str_extract_all(d14_el[-1], "\\d+")
  for (j in seq_along(pos_vals)) {
    addresses <- as.character(obtain_masked_val2(mask, pos_vals[[j]][1]))
    for (a in addresses) mem[a] <- as.numeric(pos_vals[[j]][2])
  }
}
unlist(mem) %>% sum()
