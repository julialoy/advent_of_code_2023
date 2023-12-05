with open('day_04_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

total_points = 0
for line in raw_input:
    card_num_str, numbers = line.split(": ")
    winning_nums, elf_nums = numbers.split(" | ")
    winning_nums = winning_nums.split(" ")
    elf_nums = elf_nums.split(" ")
    total_num_matches = 0
    point_subtotal = 0
    for num in elf_nums:
        if num == '':
            continue
        elif num in winning_nums:
            total_num_matches += 1
    
    while total_num_matches > 0:
        if point_subtotal == 0:
            point_subtotal = 1
        else:
            point_subtotal = point_subtotal + point_subtotal
        total_num_matches -= 1
    total_points += point_subtotal

print(total_points)
