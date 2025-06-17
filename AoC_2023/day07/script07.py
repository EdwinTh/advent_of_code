from scipy.stats import rankdata
with open('data07.txt') as d:
    data = [el.strip().split(" ") for el in d.readlines()]

bids = [int(d[1]) for d in data]
cards = [d[0] for d in data]

def cards_to_dict(cards):
    d = {}
    for c in cards:
        d.setdefault(c, 0)
        d[c] += 1
    return d

def count_to_handscore(d):
    values_sorted = "".join([str(s) for s in sorted(d.values())])
    hands = {"5":1,"14":2, "23":3, "113":4, "122":5, "1112":6, "11111":7}
    return str(hands[values_sorted])

def card_score(c):
    s = {"A":"01", "K":"02", "Q":"03", "J":"04", "T":"05", "9":"06", "8":"07", "7":"08", "6":"09", "5":"10", "4":"11", "3":"12", "2":"13"}
    return s[c]

def cards_score(cards):
    d = cards_to_dict(cards)
    score = count_to_handscore(d)
    for c in cards:
        score += card_score(c)
    return score

s = [cards_score(c) for c in cards]
scores_raw = rankdata([cards_score(c) for c in cards])
scores = [len(cards) - int(sr) for sr in scores_raw]

for i in range(len(cards)):
    print(cards[i], '-', s[i], '-', scores_raw[i], '-', scores[i])

print("Star 1:", str(sum([s*b for s,b in zip(scores, bids)])))

