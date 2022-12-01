with open("data4.txt") as d:
    data = d.readlines()

data_splitted = [d.strip().split(" ") for d in data]
def count_unique(ll):
    return sum([1 for d in ll if len(set(d)) == len(d)])

print("star 1: " + str(count_unique(data_splitted)))

def sort_word(w):
    return "".join(sorted(w))

def sort_words_list(l):
    return [sort_word(w) for w in l]

data_sorted = [sort_words_list(l) for l in data_splitted]
print("star 2: " + str(count_unique(data_sorted)))