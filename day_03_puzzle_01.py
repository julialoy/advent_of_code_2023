with open('day_03_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

puzzle_input = [list(line) for line in raw_input]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~', '/', '\\', '?', ',', ';', ':', '{', '}', '[', ']', '|', '\'', '\"']

sum_of_part_nums = 0
for y in range(len(puzzle_input)):
    x = 0
    while x < len(puzzle_input[y]):
        end_num = x
        is_digit = False
        is_valid_part_num = False
        if puzzle_input[y][x].isdigit():
            is_digit = True
            z = x+1
            while z < len(puzzle_input[y]) and puzzle_input[y][z].isdigit():
                end_num = z
                z += 1
        
        if is_digit:
            for u in range(x, end_num+1):
                if y-1 >= 0 and puzzle_input[y-1][u] in symbols:
                    is_valid_part_num = True
            for d in range(x, end_num+1):
                if y+1 < len(puzzle_input) and puzzle_input[y+1][d] in symbols:
                    is_valid_part_num = True
            if x-1 > 0 and y-1 > 0 and puzzle_input[y-1][x-1] in symbols:
                is_valid_part_num = True
            if end_num+1 < len(puzzle_input[y]) and y-1 > 0 and puzzle_input[y-1][end_num+1] in symbols:
                is_valid_part_num = True
            if x-1 > 0 and puzzle_input[y][x-1] in symbols:
                is_valid_part_num = True
            if end_num+1 < len(puzzle_input[y]) and puzzle_input[y][end_num+1] in symbols:
                is_valid_part_num = True
            if x-1 > 0 and y+1 < len(puzzle_input) and puzzle_input[y+1][x-1] in symbols:
                is_valid_part_num = True
            if end_num+1 < len(puzzle_input[y]) and y+1 < len(puzzle_input) and puzzle_input[y+1][end_num+1] in symbols:
                is_valid_part_num = True
        
            if is_valid_part_num:
                temp_num_str = ""
                for i in range(x, end_num+1):
                    temp_num_str = temp_num_str + puzzle_input[y][i]
                sum_of_part_nums += int(temp_num_str)

        if is_valid_part_num:
            x = end_num + 1
        else:
            x += 1

print(sum_of_part_nums)
            
        