# We are given a string and need to split in into 'halves' to get our compartments
# The first half of our string is compartment 1
# The second half of our string is compartment 2
# If an item is not sorted properly it will appear in both compartments
# Once the item is found we need to give it a priority number
# a-z will be priority 1-26, and A-Z will be 27-52
# After all the items have been found we want the sum of their priority numbers

def get_priority_string(filename):
    """Reads lines from a file and creates a set of two slices.
    Uses intersection on the two sets to find the item common to both slices
    Uses pop() to concatenate the common item to our priority string
    Returns a priority string containing all items that need to be sorted
    """
    prioritystr = ''
    with open(filename, 'r') as infile:
        for line in infile:
            compartment_one = set(line[:len(line)//2])
            compartment_two = set(line[len(line)//2:])
            items_in_both = compartment_one.intersection(compartment_two)
            prioritystr += items_in_both.pop()

        return prioritystr

def get_priority_sum(filename):
    """This function calls get_priority_string(filename) to get a priority string
    Then loops through that string, using a dictionary to calculate priority values.
    Returns a total sum of priority values from prioritys in the priority string"""
    prioritystr = get_priority_string(filename)
    priority_sum = 0
    priority_map = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }
    for priority in prioritystr:
        priority_sum += priority_map[priority]
    return priority_sum

print(get_priority_sum('rucksackdata.txt'))


        

