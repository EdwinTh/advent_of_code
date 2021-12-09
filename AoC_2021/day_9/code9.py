lines = [line.strip() for line in open('data9.txt')]
ncol = len(lines[0])
nrow = len(lines)
nrs = [int(char) for line in lines for char in line]
rows = [r for r in range(nrow)] * ncol
rows.sort()
cols = [r for r in range(ncol)] * nrow
def get_adjacent(pos, rows, cols, nrs):
    rows_in_scope = [abs(r - rows[pos]) < 2 for r in rows]
    cols_in_scope = [abs(c - cols[pos]) < 2 for c in cols]
    rows_in_scope_adj = [False if i == pos else rows_in_scope[i] for i in range(len(rows))]
    cols_in_scope_adj = [False if i == pos else cols_in_scope[i] for i in range(len(rows))]
    return [nrs[i] for i in range(len(nrs)) if rows_in_scope_adj[i] and cols_in_scope_adj[i]]

local_min = []
for i in range(len(nrs)):
    adj = get_adjacent(i, rows, cols, nrs)
    if len([a for a in adj if a < nrs[i]]) == 0:
        local_min.append(nrs[i])

print(sum(local_min) + len(local_min))
