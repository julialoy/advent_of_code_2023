with open('day_05_input.txt', 'r') as f:
    raw_input = f.read().split("\n\n")


def extract_values(curr_dict):
    val_list = []
    for val in curr_dict.values():
        for x in range(len(val)):
            val_list.append(val[x])
    return val_list


def get_correlation(corr_line):
    source_start = corr_line[1]
    dest_start = corr_line[0]
    step = corr_line[2]
    source_end = source_start + (step - 1)
    dest_end = dest_start + (step - 1)
    return {'source_start': source_start, 'source_end': source_end,
            'dest_start': dest_start, 'dest_end': dest_end}


def get_range(given_range, source_range):
    start_offset = given_range['source_end'] - source_range[0]
    end_offset = given_range['source_end'] - source_range[1]
    new_val_start = given_range['dest_end'] - start_offset
    new_val_end = given_range['dest_end'] - end_offset
    return new_val_start, new_val_end


def build_range(remaining_range, range_dict):
    # Source_item completely in current range
    in_range = None
    if remaining_range[0] >= range_dict['source_start'] and remaining_range[1] <= range_dict['source_end']:
        in_range = get_range(range_dict,
                             (remaining_range[0], remaining_range[1]))
        remaining_range = [-1, -1]
    # Source_item starts lower than current range but ends within current range
    elif remaining_range[0] < range_dict['source_start'] and range_dict['source_start'] <= remaining_range[1] <= range_dict['source_end']:
        in_range = get_range(range_dict,
                             (range_dict['source_start'], remaining_range[1]))
        remaining_range[1] = range_dict['source_start'] - 1
    # Source_item start is within current range but ends outside current range
    elif range_dict['source_start'] <= remaining_range[0] <= range_dict['source_end'] and remaining_range[1] > range_dict['source_end']:
        in_range = get_range(range_dict,
                             (remaining_range[0], range_dict['source_end']))
        remaining_range[0] = range_dict['source_end'] + 1
    # Source_item starts and ends outside current range, some values within current range
    elif remaining_range[0] < range_dict['source_start'] and remaining_range[1] > range_dict['source_end']:
        in_range = (range_dict['dest_start'], range_dict['dest_end'])
        remaining_range = [remaining_range[0], range_dict['source_start'] - 1,
                           range_dict['source_end'] + 1, remaining_range[1]]

    return in_range, remaining_range


def build_range_helper(range_list, current_range_dict):
    if len(range_list) == 2:
        range_result, remain_result = build_range(range_list, current_range_dict)
        return [range_result], remain_result

    range_obj = []
    for y in range(0, len(range_list), 2):
        range_obj.append(range_list[y])
        range_obj.append(range_list[y+1])

    range_result = []
    remain_result = []
    while len(range_obj) > 0:
        temp_1 = range_obj.pop(0)
        temp_2 = range_obj.pop(0)
        temp_result, temp_remain = build_range([temp_1, temp_2], current_range_dict)
        if temp_result:
            range_result.append(temp_result)
        if len(temp_remain) == 2:
            remain_result.append(temp_remain[0])
            remain_result.append(temp_remain[1])
        elif len(temp_remain) > 2:
            for z in range(0, len(temp_remain), 2):
                remain_result.append(temp_remain[z])
                remain_result.append(temp_remain[z+1])

    return range_result, remain_result


def build_dict(source_list, range_line_list):
    new_dict = {}
    for source_item in source_list:
        remaining_range = [source_item[0], source_item[1]]
        new_dict[source_item] = []
        range_lines_handled = False
        while remaining_range and not range_lines_handled:
            for range_line in range_line_list:
                curr_range_dict = get_correlation(range_line)

                range_map, remaining_range = build_range_helper(remaining_range, curr_range_dict)

                if range_map:
                    for new_range in range_map:
                        if new_range:
                            new_dict[source_item].append(new_range)

            range_lines_handled = True

        for r in range(0, len(remaining_range), 2):
            if remaining_range[r] != -1 and remaining_range[r+1] != -1:
                new_dict[source_item].append((remaining_range[r], remaining_range[r+1]))

    return new_dict


raw_seed_list = raw_input[0].split(": ")[1].split(" ")
seed_range_list = []
for i in range(0, len(raw_seed_list), 2):
    start_range = int(raw_seed_list[i])
    end_range = (start_range + int(raw_seed_list[i+1]) - 1)
    seed_range_list.append((start_range, end_range))

initial_seed_maps = {}
for i in range(1, len(raw_input)):
    line = raw_input[i]
    map_name, map_info = line.split(":")
    map_name = map_name.split(" ")[0]
    map_info = map_info.split("\n")
    del map_info[0]
    parsed_map_info = []
    for line in map_info:
        parsed_line = [int(num) for num in line.split(" ")]
        parsed_map_info.append(parsed_line)
    initial_seed_maps[map_name] = parsed_map_info

seed_to_soil_dict = build_dict(seed_range_list,
                               initial_seed_maps['seed-to-soil'])
seed_to_soil_values = extract_values(seed_to_soil_dict)

soil_to_fert_dict = build_dict(seed_to_soil_values,
                               initial_seed_maps['soil-to-fertilizer'])

soil_to_fert_values = extract_values(soil_to_fert_dict)

fert_to_water_dict = build_dict(soil_to_fert_values,
                                initial_seed_maps['fertilizer-to-water'])
fert_to_water_values = extract_values(fert_to_water_dict)

water_to_light_dict = build_dict(fert_to_water_values,
                                 initial_seed_maps['water-to-light'])
water_to_light_values = extract_values(water_to_light_dict)

light_to_temp_dict = build_dict(water_to_light_values,
                                initial_seed_maps['light-to-temperature'])
light_to_temp_values = extract_values(light_to_temp_dict)

temp_to_humid_dict = build_dict(light_to_temp_values,
                                initial_seed_maps['temperature-to-humidity'])
temp_to_humid_values = extract_values(temp_to_humid_dict)

humid_to_loc_dict = build_dict(temp_to_humid_values,
                               initial_seed_maps['humidity-to-location'])
humid_to_loc_values = extract_values(temp_to_humid_dict)

print(min(extract_values(humid_to_loc_dict))[0])
