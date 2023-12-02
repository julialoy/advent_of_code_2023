with open('day_01_input.txt', 'r') as f:
    raw_input = f.read().split("\n")
    puzz_input = [list(instruc) for instruc in raw_input]

calibration_value = 0
for i in range(len(puzz_input)):
    first_digit = None
    for char in puzz_input[i]:
        if char.isdigit():
            first_digit = char
            break

    last_digit = None
    for r in range(len(puzz_input[i])-1, -1, -1):
        if puzz_input[i][r].isdigit():
            last_digit = puzz_input[i][r]
            break

    calibration_value += (int(first_digit + last_digit))

print(calibration_value)
