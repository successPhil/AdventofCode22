# Supplies are in crates that are stacked
# The crates need to be re-arranged by a crane
# The crane has specific instructions for rearranging crate (crane_instructions.txt)
# We are provided with a drawing of the initial stacks of crates (initial_supplies.txt)
# Multiple crates can be moved at once, so order WILL be maintained when moving
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
    """This function takes a text file of crane instructions and a dictionary representing our initial supplies
    It then reads our instructions and performs the required crane operations on our supplies
    Returns: An updated dictionary after all crane operations have been completed"""
    with open(crane_instructions, 'r') as instructions:
        for operations in instructions:
            crane_operations = re.findall(r'\d+', operations) #Gets a list of our digits in the file with instructions
            move_from_to = [int(num) for num in crane_operations] #Converts our string digits to numbers in our list
            num_to_move = move_from_to[0] #num_to_move represents the number of boxes the crane will pick up
            starting_at = move_from_to[1] #starting_at represents the key in our dictionary that contains the list we are picking up crates from
            ending_at = move_from_to[2] #ending_at represents the key in our dictionary that the crane is moving crates to
            taking_from = supply_stacks[starting_at] #taking_from is the list in our dictionary that crates are being moved from
            moving_to = supply_stacks[ending_at] #moving_to is the list in our dictionary that the crates are being moved to

            #Variables from line 31 (num_to_move) to line 35 (moving_to) are not necessary but improve readability

            moving = taking_from[-num_to_move:] #moving creates a copy of the crates we are going to move
            del taking_from[-num_to_move:] #Now that a copy is made, we can safely delete the crates that are to be moved from the list we are taking from
            moving_to.extend(moving) #We extend our copy of the crates to be moved to the list we are instructed to move crates to
        return supply_stacks #Once all lines have been read, all operations should be complete so we return the updated dictionary



def get_top_crates(crane_instructions, supply_stacks):
    """This makes use of the function perform_crane_operations to get an updated dictionary after
    crane operations have been executed.
    Loops through our dictionary and concats the end of each list inside to a new string
    Returns: a new string represents the top of each supply stack"""
    supplies_after_operations = perform_crane_operations(crane_instructions, supply_stacks)
    top_crates = ''
    for stacklist in supplies_after_operations.values():
        top_crates += stacklist[-1]
    return top_crates
    
print(get_top_crates('crane_instructions.txt', supply_crate_stacks))    
