from pyprojroot import here
import re
# part one
with open(here("01-trebuchet/input.txt"), "r") as f:
    txt = f.read()
    f.close()
txt = txt.splitlines()
digi_pat = r"[0-9]"
search_pat = re.compile(digi_pat)
digits = []
for seq in txt:
    first = search_pat.search(seq).group(0)
    last = search_pat.search(seq[::-1]).group(0)
    digits.append(int(first + last))

print(f"The answer to part one is {sum(digits)}")
# part 2
num_words = r"one|two|three|four|five|six|seven|eight|nine"
forward = re.compile(num_words +r"|"+ digi_pat)
backward = re.compile(num_words[::-1] +r"|"+ digi_pat)
numdict = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}
digits = []
for seq in txt:
    first = forward.search(seq).group()
    last = backward.search(seq[::-1]).group()[::-1] # remember to un-reverse
    try:
        # will work if there are any words
        first = numdict[first]
    except KeyError:
        # pass if digits were found
        pass
    try:
        last = numdict[last]
    except KeyError:
        pass
    digits.append(int(first+last))

print(f"The answer to part one is {sum(digits)}")
