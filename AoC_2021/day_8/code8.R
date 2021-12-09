library(purrr)
splitted <- readLines('day_8/data8.txt') |>
  strsplit(" \\| ") 

pt1 <- map(splitted, 1) |> map(~strsplit(.x, " ") |> unlist()) |> 
  map(~strsplit(.x, ""))

mapping_from_pt1 <- function(el) {
  l <- map_int(el, length)
  l2 <- el[[which(l == 2)]]
  l3 <- el[[which(l == 3)]]
  l4 <- el[[which(l == 4)]]
  l5 <- el[which(l == 5)]
  l6 <- el[which(l == 6)]
  l7 <- el[[which(l == 7)]]
  a  <- setdiff(l3, l2)
  eg <- setdiff(l7, c(l4, l3, l2))
  e  <- names(which(table(unlist(l6))[eg] == 2))
  g  <- setdiff(eg, e)
  nr06 <- l6[map_lgl(l6, ~e %in% .x)]
  c_ <- unlist(map(nr06, ~setdiff(l2, .x)))
  d <- setdiff(names(which(table(unlist(nr06)) == 1)), c_)
  b <- setdiff(l4, c(l2, d))
  f <- setdiff(l2, c_)
  c('a' = a, 'b' = b, 'c' = c_, 'd' = d, 'e' = e, 'f' = f, 'g' = g)
}

select_sort_collapse <- function(letters, lm) {
  lm[names(lm) %in% letters] |> sort() |> paste(collapse = "")

}
number_mapping_from_p1 <- function(lm) {
  c('0' = select_sort_collapse(c('a', 'b', 'c', 'e', 'f', 'g') ,lm), 
    '1' = select_sort_collapse(c('c', 'f') ,lm), 
    '2' = select_sort_collapse(c('a', 'c', 'd', 'e', 'g') ,lm), 
    '3' = select_sort_collapse(c('a', 'c', 'd', 'f', 'g') ,lm), 
    '4' = select_sort_collapse(c('b', 'c', 'd', 'f') ,lm), 
    '5' = select_sort_collapse(c('a', 'b', 'd', 'f', 'g') ,lm), 
    '6' = select_sort_collapse(c('a', 'b', 'd', 'e', 'f', 'g') ,lm), 
    '7' = select_sort_collapse(c('a', 'c', 'f') ,lm), 
    '8' = select_sort_collapse(c('a', 'b', 'c', 'd', 'e', 'f', 'g') ,lm), 
    '9' = select_sort_collapse(c('a', 'b', 'c', 'd', 'f', 'g') ,lm)
  )
}

letter_mapping <- map(pt1,~.x |> mapping_from_pt1() |> number_mapping_from_p1())

pt2 <- map(splitted, 2) |> map(~strsplit(.x, " ") |> unlist()) |> 
  map(~strsplit(.x, "")) |> map(~map(.x, ~.x |> sort() |> paste(collapse ="")))

map2(pt2, letter_mapping, function(p2, m) map_chr(p2, ~names(m)[.x == m]))|>
  map_chr(~paste(.x, collapse = "")) |> as.integer() |> sum() |> print()
  