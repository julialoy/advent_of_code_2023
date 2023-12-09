def compare_cards(card_1, card_2):
    """
    Returns 0 if both cards are equal
    Returns -1 if card_1 is less than card_2
    Returns 1 if card_1 is greater than card_2
    """
    card_rankings = {'A': 'KQT98765432J', 'K': 'QT98765432J', 'Q': 'T98765432J',
                     'T': '98765432J', '9': '8765432J', '8': '765432J',
                     '7': '65432J', '6': '5432J', '5': '432J', '4': '32J', '3': '2J', '2': 'J',
                     'J': ''}
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


def sort_hands_into_type(card_num_list, total_cards_by_type):
    high_card = card_num_list[0] if card_num_list else -1
    if high_card == 5:
       return 'five_kind'
    elif high_card == 4 and total_cards_by_type['J'] == 0:
        return 'four_kind'
    elif high_card == 4 and total_cards_by_type['J'] == 1:
        total_cards_by_type['J'] -= 1
        return 'five_kind'
    elif high_card == 3 and total_cards_by_type['J'] == 2:
        total_cards_by_type['J'] -= 2
        return 'five_kind'
    elif high_card == 3 and total_cards_by_type['J'] == 1:
        total_cards_by_type['J'] -= 1
        return 'four_kind'
    elif high_card == 3 and 2 in card_num_list[1:]:    # If this case is reached, no jokers
        return 'full'
    elif high_card == 3 and 2 not in card_num_list[1:]:
        return 'three_kind'
    elif high_card == 2 and total_cards_by_type['J'] == 3:
        total_cards_by_type['J'] -= 3
        return 'five_kind'
    elif high_card == 2 and total_cards_by_type['J'] == 2:
        total_cards_by_type['J'] -= 2
        return 'four_kind'
    elif high_card == 2 and total_cards_by_type['J'] == 1 and 2 in card_num_list[1:]:
        total_cards_by_type['J'] -= 1
        return'full'
    elif high_card == 2 and total_cards_by_type['J'] == 1 and 2 not in card_num_list[1:]:
        total_cards_by_type['J'] -= 1
        return 'three_kind'
    elif high_card == 2 and 2 in card_num_list[1:]:  # if this is reached, no jokers left
       return 'two_pair'
    elif high_card == 2 and 2 not in card_num_list[1:]:
        return 'one_pair'
    elif high_card == 1 and total_cards_by_type['J'] == 4:
        total_cards_by_type['J'] -= 4
        return 'five_kind'
    elif high_card == 1 and total_cards_by_type ['J'] == 3:
        total_cards_by_type['J'] -= 3
        return 'four_kind'
    elif high_card == 1 and total_cards_by_type['J'] == 2:
        total_cards_by_type['J'] -= 2
        return 'three_kind'
    elif high_card == 1 and total_cards_by_type['J'] == 1:
        total_cards_by_type['J'] -= 1
        return 'one_pair'
    elif high_card == 1:
        return 'high_card'

    if total_cards_by_type['J'] == 5:
        return 'five_kind'


with open('day_07_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

puzzle_input = [[line.split(" ")[0], int(line.split(" ")[1])] for line in raw_input]
hand_result = {'five_kind': [], 'four_kind': [], 'full': [], 'three_kind': [],
               'two_pair': [], 'one_pair': [], 'high_card': []}
for hand in puzzle_input:
    cards_in_hand = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, 
                     '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, 
                     '4': 0, '3': 0, '2': 0}
    for c in range(len(hand[0])):
        cards_in_hand[hand[0][c]] += 1
    
    card_numbers = []
    for k,v in cards_in_hand.items():
        if v > 0 and k != 'J':
            card_numbers.append(v)
    card_numbers.sort(reverse=True)
    hand_type = sort_hands_into_type(card_numbers, cards_in_hand)
    insert_hand(hand, hand_result[hand_type])

# Ensure that dict values are in order from highest to lowest for calculating total winnings
# Due to dict order not being ensured and not using Python's OrderedDict
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
