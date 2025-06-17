import re
with open('data02.txt') as d:
    data = [el.strip() for el in d.readlines()]

REQUIRED =  {"red":12, "blue":14, "green":13}

def get_game_nr(game):
    return int(re.findall('Game (\d+)', game)[0])

def return_max_color(game, col_name):
    shows = re.findall(f'(\d+) {col_name}', game)
    return max([int(s) for s in shows])

def return_game_nr_if_valid(game):
    game_nr = get_game_nr(game)
    for col in REQUIRED.keys():
        if return_max_color(game, col) > REQUIRED[col]:
            game_nr = 0
    return game_nr

print("Star 1 =", str(sum([return_game_nr_if_valid(game) for game in data])))

def give_max_col_values(game):
    return [return_max_color(game, col) for col in REQUIRED.keys()]

def calculate_product(l):
    return l[0] * l[1] * l[2]

def get_product_of_max_vals(game):
    return calculate_product(give_max_col_values(game))

print("Star 2 =", str(sum([get_product_of_max_vals(game) for game in data])))   