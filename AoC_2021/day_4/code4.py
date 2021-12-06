# star 1
with open('data.txt') as f:
    data = f.readlines()
data = [d.strip() for d in data if d.strip() != '']

nrs = [int(d) for d in data[0].split(",")]

data_split = [d.replace("  ", " ").split(" ") for d in data[1:]]
flattened = [int(el) for row in data_split for el in row]

def nr_to_none(full_list, nr):
    return [None if f == nr else f for f in full_list]

def check_bingo_rows(flattened):
    start_inds = range(0, len(flattened) - 5, 5)
    return([si for si in start_inds if not any(flattened[si:si+5])])
   
def check_bingo_cols(flattened):
    start_inds = [r for r in range(0, len(flattened)) if r % 25 < 5]
    def subset_col_from_si(si):
        return [flattened[i] for i in range(si, si+21, 5)]
    return([si for si in start_inds if not any(subset_col_from_si(si))])

bingo = False
while not bingo:
    flattened = nr_to_none(flattened, nrs[0])
    si_bingo = check_bingo_rows(flattened) + check_bingo_cols(flattened)
    if len(si_bingo) > 0:
        break
    nrs.pop(0)

bingo_card_won = [flattened[i] for i in range(si_bingo[0], si_bingo[0] + 25)]
card_won_nrs_remaining = [nr for nr in bingo_card_won if nr is not None]

print(nrs[0] * sum(card_won_nrs_remaining))