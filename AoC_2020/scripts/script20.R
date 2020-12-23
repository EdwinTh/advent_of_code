library(tidyverse); options(scipen = 999)
d20 <- read_lines("data/data20")

# star 1
tiles  <- d20[seq(1, length(d20), 12)] %>% str_extract_all("\\d+") %>% unlist() %>% as.numeric()
images <- d20[str_detect(d20,  "#|\\.")] %>% split(rep(1:(length(.) / 10), each = 10)) %>% 
  map(~str_split(.x, "") %>% unlist() %>% matrix(nrow = 10, byrow = TRUE))
                                              
get_all_sides <- function(x) {
  sides <- list(x[1, 1:10], x[10, 1:10], x[1:10, 1], x[1:10, 10])
  c(sides, map(sides, rev))
}

compare_images <- function(x, y) {
  sides <- split(expand_grid(x = 1:8, y = 1:8), 1:64)
  sides[map_lgl(sides, ~isTRUE(all.equal(x[[ .x$x ]], y[[ .x$y ]])))] %>% 
    bind_rows()
}

image_sides <- map(images, get_all_sides)
image_nrs <- as_tibble(t(combn(1:length(images), 2))) %>% split(1:nrow(.))
matches <- map(image_nrs, ~compare_images(image_sides[[.x$V1]], image_sides[[.x$V2]])) %>% 
  map2_dfr(image_nrs, bind_cols)

dist_combs <- select(matches, V1, V2) %>% distinct()
corners <- bind_rows(dist_combs, select(dist_combs, V2 = V1, V1 = V2)) %>% count(V1) %>% filter(n == 2)
tiles[corners$V1] %>% prod()

# star 2
corner_con <- matches %>% filter(V1 %in% corners$V1 | V2 %in% corners$V1)


