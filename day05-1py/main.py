# Supplies are in crates that are stacked
# The crates need to be re-arranged by a crane
# The crane has specific instructions for rearranging crate (crane_instructions.txt)
# We are provided with a drawing of the initial stacks of crates (initial_supplies.txt)
# Crates must be moved 1 at a time by the crane
# After the crane operations are executed, the elves want to know which crates are at the top of each stack

#We are going to use regex pattern \d+ to match our digits from each line
import re

supply_crate_stacks = {
    1: ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'],
    2: ['Z', 'C', 'D'],
    3: ['H', 'J', 'F', 'C', 'N', 'G', 'W'],
    4: ['P', 'J', 'D', 'M', 'T', 'S', 'B'],
    5: ['N', 'C', 'D', 'R', 'J'],
    6: ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'],
    7: ['P', 'Z', 'T', 'F', 'R', 'H'],
    8: ['L', 'V', 'M', 'G'],
    9: ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J']
}

def perform_crane_operations(crane_instructions, supply_stacks):
    with open(crane_instructions, 'r') as infile:
        for line in infile:
            crane_operations = re.findall(r'\d+', line)
            move_from_to = [int(num) for num in crane_operations]
            num_of_moves = 0
            while num_of_moves < move_from_to[0]:
                move_crate = supply_stacks[move_from_to[1]].pop()
                supply_stacks[move_from_to[2]].append(move_crate)
                num_of_moves += 1
        return supply_stacks

    
def get_top_crates(crane_instructions, supply_stacks):
    supplies_after_operations = perform_crane_operations(crane_instructions, supply_stacks)
    top_crates = ''
    for stacklist in supplies_after_operations.values():
        top_crates += stacklist[-1]
    return top_crates
    
print(get_top_crates('crane_instructions.txt', supply_crate_stacks))    
