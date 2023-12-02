with open("day_02_input.txt", "r") as f:
    raw_input = f.read().split("\n")

puzzle_input = [line.split("; ") for line in raw_input]


def get_least_cubes(game_cubes, curr_red=0, curr_green=0, curr_blue=0):
    least_red = curr_red
    least_green = curr_green
    least_blue = curr_blue
    for cubes in game_cubes:
        cube_num, cube_color = cubes.split(" ")
        if cube_color == 'red' and int(cube_num) > least_red:
            least_red = int(cube_num)
        elif cube_color == 'green' and int(cube_num) > least_green:
            least_green = int(cube_num)
        elif cube_color == 'blue' and int(cube_num) > least_blue:
            least_blue = int(cube_num)

    return least_red, least_green, least_blue


sum_power_sets = 0
for game in puzzle_input:
    game_length = len(game)
    game_str, curr_game = game[0].split(": ")
    game_id_str = game_str.split(" ")[1]
    # Handle first set of cubes
    red, green, blue = get_least_cubes(curr_game.split(", "))

    if len(game) > 1:
        for g in range(1, len(game)):
            red, green, blue = get_least_cubes(game[g].split(", "),
                                               red, green, blue)

    sub_power = red * green * blue
    sum_power_sets += sub_power

print(sum_power_sets)
