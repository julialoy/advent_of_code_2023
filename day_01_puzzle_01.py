with open('day_01_input.txt', 'r') as f:
    raw_input = f.read().split("\n")
    puzz_input = [list(instruc) for instruc in raw_input]

calibration_value = 0
for puzz_line in puzz_input:
    first_digit = None
    last_digit = None
    first = 0
    last = len(puzz_line)-1

    while first < len(puzz_line) and last >= 0:
        if puzz_line[first].isdigit() and not first_digit:
            first_digit = puzz_line[first]

        if puzz_line[last].isdigit() and not last_digit:
            last_digit = puzz_line[last]

        first += 1
        last -= 1

    calibration_value += (int(first_digit + last_digit))

print(calibration_value)
