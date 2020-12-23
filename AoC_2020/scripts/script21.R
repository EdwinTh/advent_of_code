library(tidyverse)
d21 <- read_lines("data/data21")

# star 1
ingredients <- str_split(d21, " \\(contains ") %>% map(1) %>% 
  map(~str_split(.x, " ") %>% unlist())
allergenes  <- str_split(d21, " \\(contains ") %>% map_chr(2) %>% 
  str_replace_all("\\)", "") %>% str_split(", ")

full_mapping <- map2_dfr(ingredients, allergenes, 
                         ~expand_grid(ingr = .x, aller = .y)) %>% 
  mutate(product = rep(1:length(ingredients), 
                       map_dbl(ingredients, length) * map_dbl(allergenes, length)))

aller_count <- full_mapping %>% distinct(product, aller) %>% count(aller)
options <- full_mapping %>% count(aller, ingr) %>% inner_join(aller_count)
anti_join(full_mapping, options, by = "ingr") %>% 
  distinct(ingr, product) %>% nrow()

# star 2
assign <- character(unique(options$aller) %>% length)
names(assign) <- unique(options$aller)
while (any(assign == "")) {
  ingr_to_assign <- options %>% count(ingr) %>% filter(n == 1) %>% select(-n)
  to_assign <- inner_join(options, ingr_to_assign, by = "ingr")
  assign[to_assign$aller] <- to_assign$ingr
  options <- anti_join(options, to_assign, by = "aller")
}
paste(assign, collapse = ",")