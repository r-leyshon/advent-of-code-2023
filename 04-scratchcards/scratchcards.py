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
    card = int(card.split(" ")[-1])
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
# get the duplicate cards
card_pile = list(zip(scratchcards.keys(), win_record)) # use this to keep track
# of processed cards card pile tracks number of cards. key is card num, value
# is a list where first int is number of winning numbers, second int is number
# of cards of this type
card_pile = { k: [v, 1] for k,v in zip(scratchcards.keys(), win_record)}

for k, v in card_pile.items():
    # condition that allows addition of more cards while card count is > 0:
    while v[-1] > 0:
        n_wins = v[0]
        prize_cards = []
        for r in range(0, n_wins):
            prize_cards.append(k + 1 + r)
        
        # remove the redeemed card
        v[-1] -= 1
        # add the prize cards
        for prize in prize_cards:
            card_pile[prize][-1] += 1
            # increase the number of cards total
            n_cards += 1

print(f"The answer to part 2 is: {n_cards}")
