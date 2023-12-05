with open('day_04_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

total_scratchcards = 0
copy_dict = {}
for line in raw_input:
    card_num_str, numbers = line.split(": ")
    card_num = int(card_num_str.split(" ")[-1])
    card_num_str = "Card" + " " + str(card_num)
    winning_nums, elf_nums = numbers.split(" | ")
    winning_nums = winning_nums.split(" ")
    elf_nums = elf_nums.split(" ")
    total_num_matches = 0

    if card_num_str in copy_dict.keys():
        copy_dict[card_num_str] += 1
    else:
        copy_dict[card_num_str] = 1

    for num in elf_nums:
        if num == "":
            continue
        elif num in winning_nums:
            total_num_matches += 1
    
    num_copies = copy_dict[card_num_str]
    
    for i in range(1, total_num_matches+1):
        card = "Card" + " " + str(card_num + i)
        if card_num + i > len(raw_input):
            continue
        else:
            if card in copy_dict.keys():
                copy_dict[card] += (num_copies)
            else:
                copy_dict[card] = num_copies
        
for k, v in copy_dict.items():
    total_scratchcards += v

print(total_scratchcards)
