#Elves are given ID numbers for cleaning assignments
#They are split into pairs with each ID representing the section to clean
# Some of the pairs contain overlap, where both elves in a pair will clean some of the same things
# We want to find if any sections completely contain the sections of the other in a pair
# Need to return the number of pairs for which this is true
def count_double_work(filename):
    """Reads a file by line and splits the line on ','
    Uses the array containing resulting strings to split by '-'
    for each range in the pair
    With the beginning and ending range for each pair we compare if one contains the other
    Our counter is incremented each time this is true
    Returns: Number of times one range is fully contained within the other"""
    num_of_overlaps = 0
    with open(filename, 'r') as infile:
        for line in infile:
            line = line.strip()
            assignment_ranges = line.split(',')
            first_range = assignment_ranges[0].split('-')
            second_range = assignment_ranges[1].split('-')
            elf_one_start = int(first_range[0])
            elf_one_end = int(first_range[1])
            elf_two_start = int(second_range[0])
            elf_two_end = int(second_range[1])
            if elf_one_start >= elf_two_start and elf_one_end <= elf_two_end or elf_two_start >= elf_one_start and elf_two_end <= elf_one_end:
                num_of_overlaps += 1
        return num_of_overlaps

        
    

print(count_double_work('ranges.txt'))
