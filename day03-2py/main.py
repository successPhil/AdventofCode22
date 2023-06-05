# Need to find badge which will be the common
#item between all 3 elves in a group
# Every set of 3 lines from groupdata.txt represents a group
# Each group may have a different badge type
# Each badge will need a priority value
# a-z is priority 1-26, A-Z is 27-52
#Need to return the sum of priorities for badges

def get_group_badges(filename):
    """This function reads the file by line and assigns the line as a set to an elf until we have a group of three.
    Once a group of 3 is reached we use intersection to find the item in common between all 3 elves.
    We concatenate that value to badges and reset our counter to continue reading lines until the file has been read.
    Return: a string containing the badge of each group of 3 from our file"""
    count = 1
    badges = ''
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.strip()
            if count == 1:
                elf_one = set(line)
            elif count == 2:
                elf_two = set(line)
            elif count == 3:
                elf_three = set(line)
                groupbadge = elf_one.intersection(elf_two, elf_three)
                badges += groupbadge.pop()
                count = 0
            count += 1
        return badges
    
def get_priority_sum(filename):
    """This function calls get_group_badges(filename) to get a priority string
    Then loops through that string, using a dictionary to calculate priority values.
    Returns a total sum of priority values from prioritys in the priority string"""
    prioritystr = get_group_badges(filename)
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

print(get_priority_sum('groupdata.txt'))




        