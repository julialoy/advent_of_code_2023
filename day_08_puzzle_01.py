with open('day_08_input.txt', 'r') as f:
    raw_input = f.read().splitlines()

step_instructions = list(raw_input[0])
node_dict = {}
for line in raw_input[2:]:
    node_name, next_nodes = line.split(" = ")
    left_node = next_nodes.split(", ")[0][1:]
    right_node = next_nodes.split(", ")[1][:3]
    node_dict[node_name] = {'L': left_node, 'R': right_node}

curr_node = 'AAA'
end_node = 'ZZZ'
curr_step = 0
steps_taken = 0
while curr_node != end_node:
    # Restart steps as needed
    if curr_step >= len(step_instructions):
        curr_step = 0
    curr_node = node_dict[curr_node]['L'] if step_instructions[curr_step] == 'L' else node_dict[curr_node]['R']
    curr_step += 1
    steps_taken += 1

print(steps_taken)
