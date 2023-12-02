with open('day_02_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

puzzle_input = [line.split("; ") for line in raw_input]


def check_cubes(game_cubes):
    poss_red = 12
    poss_green = 13
    poss_blue = 14
    for cubes in game_cubes:
        cube_num, cube_color = cubes.split(" ")
        if cube_color == 'red' and int(cube_num) > poss_red:
            return False
        elif cube_color == 'green' and int(cube_num) > poss_green:
            return False
        elif cube_color == 'blue' and int(cube_num) > poss_blue:
            return False

    return True


sum_game_ids = 0
for game in puzzle_input:
    game_length = len(game)
    game_str, curr_game = game[0].split(": ")
    game_id_str = game_str.split(" ")[1]
    # Handle first set of cubes
    game_valid = check_cubes(curr_game.split(", "))

    if not game_valid:
        continue

    if game_valid and len(game) > 1:
        g = 1
        while game_valid and g < len(game):
            game_valid = check_cubes(game[g].split(", "))
            g += 1

    if game_valid:
        sum_game_ids += int(game_id_str)

print(sum_game_ids)
