#score is calculated from the following:
# Points for choosing shape: rock: 1, paper: 2, scissors: 3
# If round ends in a Win, 6 points
#If round ends in a Draw, 3 points
#If round ends in a loss, 0 points
#In first column A: Rock, B: Paper, C: Scissors
#In second column X: Rock, Y: Paper, Z: Scissors

round_outcomes = {
    "AX": 4, #Rock-Rock, draw + 3 selected Rock + 1
    "AY": 8, #Rock-Paper, win +6, selected Paper + 2
    "AZ": 3, #Rock-Scissors, loss +0, selected Sciss + 3
    "BX": 1, #Paper-Rock, loss +0, selected Rock +1
    "BY": 5, #Paper-Paper, draw +3, selected Paper +2
    "BZ": 9, #Paper-Scissors, win +6, selected Sciss +3
    "CX": 7, #Scissors-Rock, win +6, selected Rock +7
    "CY": 2, #Scissors-Paper, loss +0, selected Paper +2
    "CZ": 6, #Scissors-Scissors, draw +3, selected Scissors +3
}

def total_score(filename):
    score = 0
    roundkey = ""
    shared_file = f'../{filename}' #Created to use same file for p1/p2

    with open(shared_file, 'r') as infile:
        for line in infile:
            roundkey += line[0] + line[2]
            score += round_outcomes[roundkey]
            roundkey = ""
        return score
    
print(total_score("round-data.txt")) #score = 10941

    