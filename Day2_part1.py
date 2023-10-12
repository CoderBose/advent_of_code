def rock_paper_scissor(input):
    finalScore = 0
    for i in input:
        val = i.split(" ")
        opponent = val[0]
        user = val[1]
        print("Entered")
        finalScore += calculateScore(opponent, user)
    return finalScore

def calculateScore(opponent, user):
            score = 0
            opp = opponent
            own = user
            if own == 'X':
                score += 1
            elif own == 'Y':
                print("Entered here")
                score += 2
            else:
                score += 3
            
            if (opp == 'A' and own == 'X') or (opp == 'B' and own == 'Y') or (opp == 'C' and own == 'Z'):
                score += 3
            elif (opp == 'A' and own == 'Y') or (opp == 'B' and own == 'Z') or (opp == 'C' and own == 'X'):
                print("Entered here again")
                score += 6
            else:
                score += 0
            print("score: ", score)
            return score

    
input = open("Day2_input.txt", 'r').read().split('\n')
# print(rock_paper_scissor(input))

# input = ['A Y', 'B X', 'C Z']
print(rock_paper_scissor(input))