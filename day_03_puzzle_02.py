with open('day_03_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

puzzle_input = [list(line) for line in raw_input]


def find_number(a, b, puzzle_input=puzzle_input):
    b_start = b
    b_end = b
    num_str = ""
    while b_start >= 0 and puzzle_input[a][b_start].isdigit():
        b_start -= 1
    
    if b_start != b:
        b_start += 1

    while b_end < len(puzzle_input[y-1]) and puzzle_input[a][b_end].isdigit():
        b_end += 1
    
    if b_end != b:
        b_end -= 1

    for i in range(b_start, b_end+1):
        num_str = num_str + puzzle_input[a][i]
    
    return int(num_str)


def find_gear_ratio(y, x, puzzle_input=puzzle_input):
    num_1 = None
    num_2 = None
    has_extra_nums = False
    if y-1 >= 0 and puzzle_input[y-1][x].isdigit():
        num_1 = find_number(y-1, x)
    else:
        if y-1 >= 0 and x-1 >= 0 and puzzle_input[y-1][x-1].isdigit():
            num_1 = find_number(y-1, x-1)
        if y-1 >= 0 and x+1 < len(puzzle_input[y]) and puzzle_input[y-1][x+1].isdigit():
            num_found = find_number(y-1, x+1)
            if not num_1:
                num_1 = num_found
            else:
                num_2 = num_found
    
    if x-1 >= 0 and puzzle_input[y][x-1].isdigit():
        left_num = find_number(y, x-1)
        if not num_1:
            num_1 = left_num
        elif not num_2:
            num_2 = left_num
        else:
            has_extra_nums = True

    if x+1 < len(puzzle_input[y]) and puzzle_input[y][x+1].isdigit():
        right_num = find_number(y, x+1)
        if not num_1:
            num_1 = right_num
        elif not num_2:
            num_2 = right_num
        else:
            has_extra_nums = True
    
    if y+1 < len(puzzle_input) and puzzle_input[y+1][x].isdigit():
        down_num = find_number(y+1, x)
        if not num_1:
            num_1 = down_num
        elif not num_2:
            num_2 = down_num
        else:
            has_extra_nums = True
    else:
        if y+1 < len(puzzle_input) and x-1 >= 0 and puzzle_input[y+1][x-1].isdigit():
            down_left = find_number(y+1, x-1)
            if not num_1:
                num_1 = down_left
            elif not num_2:
                num_2 = down_left
            else:
                has_extra_nums = True
        if y+1 < len(puzzle_input) and x+1 < len(puzzle_input[y]) and puzzle_input[y+1][x+1].isdigit():
            down_right = find_number(y+1, x+1)
            if not num_1:
                num_1 = down_right
            elif not num_2:
                num_2 = down_right
            else:
                has_extra_nums = True
    
    if num_1 and num_2 and not has_extra_nums:
        return num_1 * num_2
    
    return -1
    

sum_gear_ratios = 0
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        if puzzle_input[y][x] == '*':
            gear_ratio = find_gear_ratio(y, x)
            if gear_ratio > -1:
                sum_gear_ratios += gear_ratio

print(sum_gear_ratios)
