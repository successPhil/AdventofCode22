#score is calculated from the following:
# Points for choosing shape: rock: 1, paper: 2, scissors: 3
# If round ends in a Win, 6 points
#If round ends in a Draw, 3 points
#If round ends in a loss, 0 points
#In first column A: Rock, B: Paper, C: Scissors
#In second column X: Lose, Y: Draw, Z: Win

round_outcomes = {
    "AX": 3, #Rock-Scissors Lose +0, Scissors +3
    "AY": 4, #Rock-Rock Draw +3, Rock +1
    "AZ": 8, #Rock-Paper Win +6, Paper +2
    "BX": 1, #Paper-Rock Lose +0, Rock +1
    "BY": 5, #Paper-Paper Draw +3, Paper +2
    "BZ": 9, #Paper-Scissors Win +6, Scissors +3
    "CX": 2, #Scissors-Paper Lose +0, Paper +2
    "CY": 6, #Scissors-Scissors Draw +3, Scissors +3
    "CZ": 7, #Scissors-Rock Win +6, Rock +1
}

def total_score(filename):
    score = 0
    roundkey = ""
    shared_file = f'../{filename}' #Created to share data for p1/p2

    with open(shared_file, 'r') as infile:
        for line in infile:
            roundkey += line[0] + line[2]
            score += round_outcomes[roundkey]
            roundkey = ""
        return score 
    
print(total_score("round-data.txt")) #score = 13071