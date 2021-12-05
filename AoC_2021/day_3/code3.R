collapse_and_convert <- function(x) paste(x, collapse = "") |> strtoi(2)

# star 1
data     <- readLines("day_3/data.txt") |> strsplit("") |> lapply(as.integer)
mat      <- data |> unlist() |> matrix(byrow = TRUE, ncol = length(data[[1]])) 
gamma    <- (mat |> colSums() / nrow(mat)) |> round()
epsilson <- abs(gamma - 1)
print(collapse_and_convert(gamma) * collapse_and_convert(epsilson))

# star 2
get_record <- function(mat, col = 1, rev, tie_val) {
  if (nrow(mat) == 1) return(mat[1,])
  val <- sum(mat[,col]) / nrow(mat)
  is_tie <- val == 0.5
  val <- ifelse(is_tie, tie, round(val))
  if (rev & !is_tie) val <- abs(val - 1)
  get_record(mat[mat[,col] == val,,drop = FALSE], col+1, rev, tie)
}
print(get_record(mat, rev = FALSE, tie_val = 1) |> collapse_and_convert() *
        get_record(mat, rev = TRUE, tie_val = 0) |> collapse_and_convert())