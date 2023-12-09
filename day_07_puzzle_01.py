def compare_cards(card_1, card_2):
    """
    Returns 0 if both cards are equal
    Returns -1 if card_1 is less than card_2
    Returns 1 if card_1 is greater than card_2
    """
    card_rankings = {'A': 'KQJT98765432', 'K': 'QJT98765432', 'Q': 'JT98765432',
                     'J': 'T98765432', 'T': '98765432', '9': '8765432', '8': '765432',
                     '7': '65432', '6': '5432', '5': '432', '4': '32', '3': '2', '2': ''}
    if card_1 == card_2:
        return 0
    elif card_2 in card_rankings[card_1]:
        return 1
    else:
        return -1


def compare_hands(hand_1, hand_2):
    """
    Returns 0 if both hands are equal
    Returns -1 if hand_1 is less than hand_2
    Returns 1 if hand_1 is greater than hand_2
    """
    for h in range(len(hand_1)):
        comp_result = compare_cards(hand_1[h], hand_2[h])
        if  comp_result == -1:
            return -1
        elif comp_result == 1:
            return 1
    
    return 0


def insert_hand(new_hand, ordered_hands):
    place_found = False
    i = 0
    while i < len(ordered_hands) and not place_found:
        hand_comp_result = compare_hands(new_hand[0], ordered_hands[i][0])
        if hand_comp_result == 1:
            ordered_hands.insert(i, new_hand)
            place_found = True
        i += 1
    
    if not place_found:
        ordered_hands.append(new_hand)


def calculate_winnings(rank, hand_list):
    winning_subtotal = 0
    for hand in hand_list:
        winning_subtotal += (hand[1] * rank)
        rank -= 1
    
    return winning_subtotal, rank


with open('day_07_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

puzzle_input = [[line.split(" ")[0], int(line.split(" ")[1])] for line in raw_input]

# Dict of ranking, each value is a list with the hands
# ordered within that rank.
# Example: if 3 has two hands that have 3 of a kind, T55J5 and QQQJA,
# QQQJA will be first in the value list because it has a stronger first card
hand_result = {'five_kind': [], 'four_kind': [], 'full': [], 'three_kind': [],
               'two_pair': [], 'one_pair': [], 'high_card': []}
for hand in puzzle_input:
    cards_in_hand = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, 
                     '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, 
                     '4': 0, '3': 0, '2': 0}
    for c in range(len(hand[0])):
        cards_in_hand[hand[0][c]] += 1
    
    five_kind = 0
    four_kind = 0
    num_threes = 0
    num_pairs = 0
    for k,v in cards_in_hand.items():
        if v == 5:
            five_kind += 1
        elif v == 4:
            four_kind += 1
        elif v == 3:
            num_threes += 1
        elif v == 2:
            num_pairs += 1

    if five_kind == 1:
        insert_hand(hand, hand_result['five_kind'])
    elif four_kind == 1:
        insert_hand(hand, hand_result['four_kind'])
    elif num_threes == 1 and num_pairs == 1:
        insert_hand(hand, hand_result['full'])
    elif num_threes == 1 and num_pairs == 0:
        insert_hand(hand, hand_result['three_kind'])
    elif num_threes == 0 and num_pairs == 2:
        insert_hand(hand, hand_result['two_pair'])
    elif num_threes == 0 and num_pairs == 1:
        insert_hand(hand, hand_result['one_pair'])
    else:
        insert_hand(hand, hand_result['high_card'])

# Ensure that dict values are in order from highest to lowest for calculating total winnings
ranked_hands = []
ranked_hands.append(hand_result['five_kind']) if hand_result['five_kind'] else None
ranked_hands.append(hand_result['four_kind']) if hand_result['four_kind'] else None
ranked_hands.append(hand_result['full']) if hand_result['full'] else None
ranked_hands.append(hand_result['three_kind']) if hand_result['three_kind'] else None
ranked_hands.append(hand_result['two_pair']) if hand_result['two_pair'] else None
ranked_hands.append(hand_result['one_pair']) if hand_result['one_pair'] else None
ranked_hands.append(hand_result['high_card']) if hand_result['high_card'] else None

curr_hand_rank = len(puzzle_input)
total_winnings = 0
for ranked_hand in ranked_hands:
    hand_winnings, curr_hand_rank = calculate_winnings(curr_hand_rank, ranked_hand)
    total_winnings += hand_winnings

print(total_winnings)
