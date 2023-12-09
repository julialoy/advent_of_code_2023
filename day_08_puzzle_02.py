import math

def find_end_node(start_node, node_map, step_map):
    curr_step = 0
    steps_taken = 0
    zs_found = False
    # print(f"Starting nodes: {curr_nodes}")
    while not zs_found:
        # Restart steps as needed
        if curr_step >= len(step_instructions):
            curr_step = 0

        start_node = node_map[start_node]['L'] if step_map[curr_step] == 'L' else node_map[start_node]['R']
        if start_node[2] == 'Z':
            zs_found = True
        curr_step += 1
        steps_taken += 1

    return steps_taken
 

with open('day_08_input.txt', 'r') as f:
    raw_input = f.read().splitlines()

step_instructions = list(raw_input[0])
node_dict = {}
for line in raw_input[2:]:
    node_name, next_nodes = line.split(" = ")
    left_node = next_nodes.split(", ")[0][1:]
    right_node = next_nodes.split(", ")[1][:3]
    node_dict[node_name] = {'L': left_node, 'R': right_node}

curr_nodes = [k for k in node_dict.keys() if k[2] == 'A']
steps_per_node = []
for node in curr_nodes:
    temp_steps = find_end_node(node, node_dict, step_instructions)
    steps_per_node.append(temp_steps)
    print(f"It took {temp_steps} for {node} to reach the destination")

print(math.lcm(*steps_per_node))
