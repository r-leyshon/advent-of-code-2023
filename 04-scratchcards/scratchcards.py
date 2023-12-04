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

# find the winning nums
points_record = []
for k, v in scratchcards.items():
    points = 0
    # iterate through the nums and check against winners
    win_nums = set(v[0]) & set(v[1])
    if len(win_nums) > 0:
        points = 1
        # discount the first win that scores one point
        for _ in range(1, len(win_nums)):
            points *= 2
    else:
        points = 0
    points_record.append(points)
    
print(f"The answer to part 1 is: {sum(points_record)}")
