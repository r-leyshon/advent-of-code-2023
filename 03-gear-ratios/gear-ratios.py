import re
from pyprojroot import here
with open(here("03-gear-ratios/input.txt")) as f:
    txt = f.read()
    f.close()
# txt = txt.splitlines()
# get unique characters to inform regex
"".join(set(txt))
# +34%9.56\n8102-7&@/$*#=
# symbols are +%-&@/$*#=
# testing results in pattern: [+%&@/$*#=-] https://regex101.com/r/qBqt93/1
txt = txt.splitlines()
sym_pat = re.compile(r"[+%&@/$*#=-]")
N_ROWS = len(txt)


def find_adjacent_qualifying_numbers(window:str)->tuple:
    """Extract the qualifying numbers from string windows adjacent to a symbol.

    Parameters
    ----------
    window : str
        Any window in lines preceding or following an adjacent symbol.

    Returns
    -------
    tuple
        Qualifying numbers.
    """
    top_nums = (0, 0)
    if window[2:5] == "...":
        "..."
        pass
    elif (window[2] != ".") and (window[3] != ".") and (window[4] != "."):
        "DDD"
        top_nums = (int(window[2:5]), 0)
    elif (window[2] != ".") and (window[3] == ".") and (window[4] != "."):
        "D.D"
        top_nums = (int(window[0:3].split(".")[-1]), int(window[4:].split(".")[0]))
    elif window[2:4] == "..":
        "..D"
        top_nums = (0, int(window[4:7].split(".")[0]))
    elif window[3:5] == "..":
        "D.."
        top_nums = (int(window[0:3].split(".")[-1]), 0)
    elif window[2] == "." and window[3:5] != "..":
        ".DD"
        top_nums = (0, int(window[3:6].split(".")[0]))
    elif window[4] == "." and window[2:4] != "..":
        "DD."
        top_nums = (int(window[0:4].split(".")[-1]), 0)
    else:
        "?"
        print("Not caught!!")
        pass
    return top_nums


all_parts = []
for i, line in enumerate(txt):
    for match in sym_pat.finditer(line):
        left_num = 0
        right_num = 0
        sym_ind = match.span()[0]
        # get the qualifying window to search
        left_ind = sym_ind - 3
        right_ind = sym_ind + 4
        if i == 0:
            # avoid negative indexing
            top_window = "......."
        else:
            top_window = txt[i - 1][left_ind:right_ind]
        if i == N_ROWS:
            # avoid out of range key error
            bottom_window = "......."
        else:
            bottom_window = txt[i + 1][left_ind:right_ind]
        # get the qualifying part nums inline with the symbol
        sym_window = line[left_ind:right_ind]
        if sym_window[2] != ".":
            left_num = int(sym_window[0:3].split(".")[-1])
        if sym_window[4] != ".":
            right_num = int(sym_window[4:].split(".")[0])
        sym_nums = [left_num, right_num]
        found_inline = [n for n in sym_nums if n != ""]
        # now get the qualifying part nums for the previous and next rows
        found_above = find_adjacent_qualifying_numbers(top_window)
        found_below = find_adjacent_qualifying_numbers(bottom_window)
        all_parts.extend(found_above)
        all_parts.extend(found_inline)
        all_parts.extend(found_below)

all_parts = [part for part in all_parts if part > 0]
print(f"The solution to part one is {sum(all_parts)}")
# Part two: Find gear ratios

gear_pat = re.compile(r"[*]")
gear_ratios = []



for i, line in enumerate(txt):
    this_ratio = []
    if "*" in line:
        for match in gear_pat.finditer(line):
            left_num = 0
            right_num = 0
            sym_ind = match.span()[0]
            # get the qualifying window to search
            left_ind = sym_ind - 3
            right_ind = sym_ind + 4
            if i == 0:
                # avoid negative indexing
                top_window = "......."
            else:
                top_window = txt[i - 1][left_ind:right_ind]
            if i == N_ROWS:
                # avoid out of range key error
                bottom_window = "......."
            else:
                bottom_window = txt[i + 1][left_ind:right_ind]
            # get the qualifying part nums inline with the symbol
            sym_window = line[left_ind:right_ind]
            if sym_window[2] != ".":
                left_num = int(sym_window[0:3].split(".")[-1])
            if sym_window[4] != ".":
                right_num = int(sym_window[4:].split(".")[0])
            sym_nums = [left_num, right_num]
            found_inline = [n for n in sym_nums if n != ""]
            # now get the qualifying part nums for the previous and next rows
            found_above = find_adjacent_qualifying_numbers(top_window)
            found_below = find_adjacent_qualifying_numbers(bottom_window)


        this_ratio.extend(found_above)
        this_ratio.extend(found_inline)
        this_ratio.extend(found_below)


        this_ratio = [n for n in this_ratio if n > 0]
        print(this_ratio)
        if len(this_ratio) == 2:
            ratio = this_ratio[0] * this_ratio[-1]
            gear_ratios.append(ratio)

# gear_ratios = [part for part in gear_ratios if part > 0]
print(f"The solution to part two is {sum(gear_ratios)}")


# 348873
# 5206506
# 5964138
# 35698225
# 29120097
# 33103468



