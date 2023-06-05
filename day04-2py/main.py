# Need to find the count of any pairs that overlap at all
# Should be able to adjust our conditional from previous problem replacing and with or

def count_double_work(filename):
    """Reads a file by line and splits the line on ','
    Uses the array containing resulting strings to split by '-'
    for each range in the pair
    With the beginning and ending range for each pair we compare if it is not possible to overlap
    Our counter is incremented each time our ranges do not meet the conditions to NOT overlap
    Returns: Number of times our range pairs contain an overlap of any kind"""
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
            if not (elf_one_start > elf_two_end or elf_one_end < elf_two_start or elf_two_start > elf_one_end or elf_two_end < elf_one_start):
                num_of_overlaps += 1
        return num_of_overlaps

        
    

print(count_double_work('ranges.txt'))
