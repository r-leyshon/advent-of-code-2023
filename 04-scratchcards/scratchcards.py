from pyprojroot import here

with open(here("04-scratchcards/input.txt"), "r") as f:
    txt = f.read()
    f.close()
    
txt = txt.splitlines()
# sort out the scratchcards:
scratchcards = {}
for card in txt:
    winners, nums = card.split(" | ")
    card, winners = winners.split(": ")
    winners = winners.split(" ")
    nums = nums.split(" ")
    # converts to ints
    winners = [int(n) for n in winners if n != ""]
    nums = [int(n) for n in nums if n != ""]
    scratchcards[card] = [winners, nums]


def count_winning_numbers(card_dict: dict) -> list:
    """Get the number of times each scratchcard wins."""
    out = []
    for k, v in card_dict.items():
        # check nums against winners
        n_wins = len(set(v[0]) & set(v[1]))
        out.append(n_wins)
    return out


win_record = count_winning_numbers(scratchcards)
# find the winning nums
points_record = []
for r in win_record:
    if r > 0:
        points = 1
        for _ in range(1, r):
            points *=2
    else:
        points = 0
    points_record.append(points)
    
print(f"The answer to part 1 is: {sum(points_record)}")
# part 2

n_cards = len(txt)

