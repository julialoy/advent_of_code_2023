with open('day_01_input.txt', 'r') as f:
    raw_input = f.read().split("\n")

digit_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
              "six": "6", "seven": "7", "eight": "8", "nine": "9"}

calibration_value = 0
for puzz in raw_input:
    first_digit = None
    first_digit_ind = -1
    last_digit = None
    last_digit_ind = -1
    first = 0
    last = len(puzz) - 1

    while first < len(puzz) and last >= 0:
        if puzz[first].isdigit() and not first_digit:
            first_digit = puzz[first]
            first_digit_ind = first

        if puzz[last].isdigit() and not last_digit:
            last_digit = puzz[last]
            last_digit_ind = last

        first += 1
        last -= 1

    for k,v in digit_dict.items():
        first_target_ind = puzz.find(k)
        last_target_ind = puzz.rfind(k)
        if first_target_ind != -1 and first_target_ind < first_digit_ind:
            first_digit = v
            first_digit_ind = first_target_ind
        if first_digit_ind == -1 and first_target_ind != -1:
            first_digit = v
            first_digit_ind = first_target_ind

        if (first_target_ind != last_target_ind and
                last_target_ind != -1 and
                last_target_ind > last_digit_ind):
            last_digit = v
            last_digit_ind = last_target_ind
        elif first_target_ind != -1 and first_target_ind > last_digit_ind:
            last_digit = v
            last_digit_ind = first_target_ind

    calibration_value += int(first_digit + last_digit)

print(calibration_value)
