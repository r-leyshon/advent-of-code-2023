from pyprojroot import here
import pandas as pd

def read_and_process_cards(pth):
    all_games = []
    with open(pth, "r") as f:
        txt = f.read()
        f.close()
    txt = txt.splitlines()
    for i in txt:
        hand, bid = i.split(" ")
        bid = int(bid)
        all_games.append([hand, bid])
    return all_games
example_pth = here("07-camel-cards/example.txt")
# example_games = read_and_process_cards(example_pth)
input_pth = here("07-camel-cards/input.txt")
input_games = read_and_process_cards(input_pth)


def get_hand_worth(games: list):
    """Get the worth of each hand based on unique characters."""
    HAND_TYPE_MAP = {
        # maps outcome of hand type logic to numerical order
        1: 7,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
        7: 1,
    }
    worth = []
    def _get_character_num_appearances(char, _str):
        return len([i for i in _str if i == char])
    for game in games:
        # get unique characters in hand
        unique_chars = set(game[0])
        n_chars = len(unique_chars)
        if n_chars in [1, 4, 5]:
            # Five of a kind, One pair or High card
            if n_chars == 1:
                hand_worth = HAND_TYPE_MAP[n_chars]
            elif n_chars == 4:
                hand_worth = HAND_TYPE_MAP[6]
            elif n_chars == 5:
                hand_worth = HAND_TYPE_MAP[7]
        elif n_chars == 2:
            # Four of a kind | Full house
            first_char = list(unique_chars)[0]
            n_appearances = _get_character_num_appearances(first_char, game[0])
            # n_appearances = len([i for i in game[0] if i == first_char])
            if n_appearances in [4, 1]:
                # Four of a kind
                hand_worth = HAND_TYPE_MAP[2]
            else:
                # Full house
                hand_worth = HAND_TYPE_MAP[3]
        elif n_chars == 3:
            # Three of a kind | Two pair
            char_counts = []
            for char in unique_chars:
                n_appearances = _get_character_num_appearances(char, game[0])
                # n_appearances = len([i for i in game[0] if i == char])
                char_counts.append(n_appearances)
            if 3 in char_counts:
                # Three of a kind
                hand_worth = HAND_TYPE_MAP[4]
            else:
                # Two pair
                hand_worth = HAND_TYPE_MAP[5]
        else:
            raise Exception(f"Not caught hand {game[0]}")

        # append the hand's worth to the game_list
        worth.append(hand_worth)

    return worth


# hand_worths = get_hand_worth(example_games)
hand_worths = get_hand_worth(input_games)


def rank_hands_into_df(some_games:list, their_worth:list):
    """Creates a df of all hands ranked by their worth, calculates winnings."""
    CARD_VALUE_MAP = {
        "A": 14, 
        "K": 13, 
        "Q": 12, 
        "J": 11, 
        "T": 10, 
        "9": 9, 
        "8": 8, 
        "7": 7, 
        "6": 6, 
        "5": 5, 
        "4": 4, 
        "3": 3,
        "2": 2
        }
    game_df = pd.DataFrame()
    card_sorts_colnms = [f"sort_{i}" for i in range(2, len(some_games[0][0]) + 1)]
    for i, games in enumerate(zip(some_games, their_worth)):
        hand_dict = {}
        # print(games)
        cards = [*games[0][0]]
        card_vals = [CARD_VALUE_MAP[c] for c in cards]
        # print(card_vals)
        hand_dict["hand"] = games[0][0]
        hand_dict["bid"] = games[0][1]
        hand_dict["sort_1"] = games[-1]
        for i, colnm in enumerate(card_sorts_colnms):
            hand_dict[colnm] = card_vals[i]
        # print(hand_dict)
        row = pd.DataFrame(hand_dict, index=[i])
        # print(row)
        game_df = pd.concat([game_df, row])

    # sort by rank columns only
    game_df = game_df.sort_values(by=[c for c in game_df.columns if c.startswith("sort_")],axis=0)
    game_df = game_df.reset_index(drop=True)
    # include an index column
    game_df = game_df.reset_index()
    # ranks should start at 1
    game_df["index"] = game_df["index"]+1
    game_df["winnings"] = game_df["index"] * game_df["bid"]

    return game_df


# sorted_hand = rank_hands_into_df(example_games, hand_worths) # correct
sorted_hand = rank_hands_into_df(input_games, hand_worths)
print(f"The solution to part 1 is {sum(sorted_hand['winnings'])}")
# 248569442 too low 
