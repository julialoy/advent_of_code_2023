with open('day_05_input.txt', 'r') as f:
    raw_input = f.read().split("\n\n")


def get_correlation(corr_line):
    source_start = corr_line[1]
    dest_start = corr_line[0]
    step = corr_line[2]
    source_end = source_start + (step - 1)
    dest_end = dest_start + (step - 1)
    return {'source_start': source_start, 'source_end': source_end,
            'dest_start': dest_start, 'dest_end': dest_end}


def build_dict(source_list, range_line_list):
    new_dict = {}
    for source_item in source_list:
        new_dict[source_item] = source_item
        for range_line in range_line_list:
            range_dict = get_correlation(range_line)
            if (source_item >= range_dict['source_start'] and source_item <= range_dict['source_end']
            ):
                offset = range_dict['source_end'] - source_item
                new_val = range_dict['dest_end'] - offset
                new_dict[source_item] = new_val
    return new_dict


initial_seeds_list = [int(seed)
                      for seed
                      in raw_input[0].split(": ")[1].split(" ")]
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

seed_to_soil_dict = build_dict(initial_seeds_list,
                               initial_seed_maps['seed-to-soil'])
soil_to_fert_dict = build_dict(seed_to_soil_dict.values(),
                               initial_seed_maps['soil-to-fertilizer'])
fert_to_water_dict = build_dict(soil_to_fert_dict.values(),
                                initial_seed_maps['fertilizer-to-water'])
water_to_light_dict = build_dict(fert_to_water_dict.values(),
                                 initial_seed_maps['water-to-light'])
light_to_temp_dict = build_dict(water_to_light_dict.values(),
                                initial_seed_maps['light-to-temperature'])
temp_to_humid_dict = build_dict(light_to_temp_dict.values(),
                                initial_seed_maps['temperature-to-humidity'])
humid_to_loc_dict = build_dict(temp_to_humid_dict.values(),
                               initial_seed_maps['humidity-to-location'])

print(min(humid_to_loc_dict.values()))
