# star 1

data <- readLines("day_4/data.txt")
nrs  <- strsplit(data[1], ",") |> unlist() |> as.integer()
cards_raw <- data[-c(1:2)][data[-c(1:2)] != ""]
cards_clean <- gsub("  ", " ", cards_raw) |> strsplit(" ") |>
  lapply(function(x) x[x!=""] |> as.integer())
cards <- split(cards_clean, rep(1:(length(cards_clean) / 5), each = 5)) |>
  lapply(function(x) unlist(x) |> matrix(byrow = TRUE, nrow = 5))

cross_nr_card <- function(card, nr) {
  card[card == nr] <- NA
  card
}

check_bingo <- function(card) {
  if (any(colSums(is.na(card)) == 5) | any(rowSums(is.na(card)) == 5))
    return(card)
}

star_1 <- function(data, nrs){
  while (TRUE) {
    cards <- lapply(cards, cross_nr_card, nrs[1])
    bingo <- lapply(cards, check_bingo)
    if (!all(sapply(bingo, is.null))) {
      break
    }
    nrs <- nrs[-1] 
  }
  unlist(bingo[!sapply(bingo, is.null)]) |> sum(na.rm = TRUE) * nrs[1]
}

star_1(data, nrs)

# star 2
star_2 <- function(data, nrs) {
  while (TRUE) {
    last_bingo <- lapply(cards, check_bingo)
    cards <- lapply(cards, cross_nr_card, nrs[1])
    bingo <- lapply(cards, check_bingo)
    if (sum(sapply(bingo, is.null)) == 0) {
      break
    }
    nrs <- nrs[-1] 
  }
  cards[[which(sapply(last_bingo, is.null))]] |> sum(na.rm = TRUE) * nrs[1]
}

star_2(data, nrs)