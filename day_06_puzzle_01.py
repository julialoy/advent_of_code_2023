with open('day_06_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

raw_time_input = raw_input[0].split(": ")[1].split(" ")
time_input = [int(t) for t in raw_time_input if t != ""]
raw_dist_input = raw_input[1].split(": ")[1].split(" ")
dist_input = [int(d) for d in raw_dist_input if d != ""]

races = []
for x in range(len(time_input)):
    races.append((time_input[x], dist_input[x]))


def boat_dist_traveled(time_btn_held, total_race_time):
    return (total_race_time - time_btn_held) * time_btn_held

ways_to_win = 1
for race in races:
    total_time = race[0]
    min_winning_dist = race[1] + 1
    
    dist_max_time = boat_dist_traveled(total_time, total_time)
    max_time_btn_held = total_time - 1
    test_boat_dist = boat_dist_traveled(max_time_btn_held, total_time)
    while test_boat_dist > dist_max_time and max_time_btn_held > 0 and test_boat_dist < min_winning_dist:
        dist_max_time = test_boat_dist
        max_time_btn_held -= 1
        test_boat_dist = boat_dist_traveled(max_time_btn_held, total_time)
    
    boat_dist = 1
    min_btn_held_time = 1
    while boat_dist < min_winning_dist and min_btn_held_time <= (total_time - 1):
        min_btn_held_time += 1
        boat_dist = boat_dist_traveled(min_btn_held_time, total_time)
    
    num_ways_to_win = max_time_btn_held - min_btn_held_time + 1
    ways_to_win = ways_to_win * num_ways_to_win

print(ways_to_win)
