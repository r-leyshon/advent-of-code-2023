from pyprojroot import here
from numpy import prod
with open(here("06-wait-for-it/input.txt"), "r") as f:
    txt = f.read()
    f.close()

txt = txt.splitlines()
times = [t for t in txt[0].split(" ") if t != ""][1:]
times = [int(t) for t in times]
distances = [d for d in txt[-1].split(" ") if d != ""][1:]
distances = [int(d) for d in distances]


def get_win_options(times:list, distances:list) -> list:
    races = zip(times, distances)
    n_wins = []
    for race in races:
        speed = 0
        race_wins = 0
        # increment speed & check if this will exceed distance record
        for s in range(0, (race[0])):
            speed +=1
            remaining_time = race[0] - speed
            if speed * remaining_time > race[-1]:
                race_wins += 1
            else:
                pass
        n_wins.append(race_wins)
    
    return n_wins


n_wins = get_win_options(times=times, distances=distances)
print(f"The answer to part one is {prod(n_wins)}")
# part 2 - collapse the poorly kerned(!) races
