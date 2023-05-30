def elf_calorie_total_list(filename):
    #Open file as read
    with open(filename, 'r') as infile:
        #initialize a variable as a empty list to hold sums
        #initialize a sum variable starting at 0
        elves_calorie_totals = []
        elf_calorie_sum = 0
        #loop through the file to grab data
        for line in infile:
            #remove any extra whitespace
            line = line.strip()
            #check if anything exists on current line, if it does cast int() on that line
            #and add it to our sum
            if line:
                elf_calorie_sum += int(line)
            #If nothing exists on our current line, we have reached the last value of an elf inventory
            #So we will append our sum to our list of sums and set our sum back to 0
            else:
                elves_calorie_totals.append(elf_calorie_sum)
                elf_calorie_sum = 0
        #Once our loop ends we have an array with each index containing the sum of an elf

    #By using max() we can find the greatest sum in our array
    #We can add this to our variable for top three totals
    #Then we can use index() on that number to get an index for pop()
    
    top_three_totals = 0
    elf_with_most = max(elves_calorie_totals)
    top_three_totals += elf_with_most
    greatest_idx = elves_calorie_totals.index(elf_with_most)
    elves_calorie_totals.pop(greatest_idx)

    elf_with_second_most = max(elves_calorie_totals)
    top_three_totals += elf_with_second_most
    second_greatest_idx = elves_calorie_totals.index(elf_with_second_most)
    elves_calorie_totals.pop(second_greatest_idx)

    elf_with_third_most = max(elves_calorie_totals)
    top_three_totals += elf_with_third_most
    
    return f"The elf with the most calories had a total of {elf_with_most} and the amount of calories gathered by the top three elves was a total of {top_three_totals}"
    
print(elf_calorie_total_list('elf_data.txt'))


