from pyprojroot import here
import re

with open(here("02-cube-conundrum/input.txt"), "r") as f:
    txt = f.read()
    f.close()
txt = txt.splitlines()
# sort the IDs and games into a dict
gamedict = {}
ids = []
for i in txt:
    id, games = i.split(":")
    id = int(id.removeprefix("Game "))
    ids.append(id)
    games = games.split(";")
    gamedict[id] = games

# use regex positive lookahead to get counts of coloured cubes
red_pat = re.compile(r"[0-9]+(?= red)")
green_pat = re.compile(r"[0-9]+(?= green)")
blue_pat = re.compile(r"[0-9]+(?= blue)")
# the total numbers of cubes
total_red = 12
total_green = 13
total_blue = 14 
# helper func from re -> int


def convert_match_to_int(m:re.Match)->int:
    "Convert matches to ints, handles None to 0"
    if m is None:
        n = 0
    else:
        n = int(m.group())
    return n


possible_games = ids
for id, games in gamedict.items():
    for game in games:
        n_reds = red_pat.search(game)
        n_greens = green_pat.search(game)
        n_blues = blue_pat.search(game)
        # convert to ints
        n_reds = convert_match_to_int(n_reds)
        n_greens = convert_match_to_int(n_greens)
        n_blues = convert_match_to_int(n_blues)
        # are the games possible?
        is_poss = True
        if any([(n_reds > total_red) or (n_greens > total_green) or (n_blues > total_blue)]):
            is_poss = False
        # there are cases where multiple draws would rule out a game, so try
        if not is_poss:
            try:
                possible_games.remove(id)
            except ValueError:
                pass

print(f"The answer to part one is {sum(possible_games)}")