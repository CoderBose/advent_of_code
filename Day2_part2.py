def rock_paper_scissor(input):
    finalScore = 0
    for i in input:
        val = i.split(" ")
        opponent = val[0]
        round = val[1]
        finalScore += calculateScore(opponent, round)
    return finalScore

def calculateScore(opponent, round):
            score = 0
            opp = opponent

            if round == 'X': #lose
                score += 0
                if opp == 'A': #rock -- scissors
                    score += 3
                elif opp == 'B': #paper -- rock
                    score += 1
                else: #scissors -- paper
                    score += 2

            elif round == 'Y': #draw
                score += 3
                if opp == 'A':
                    score += 1
                elif opp == 'B':
                    score += 2
                else:
                    score += 3

            else: #win
                score += 6
                if opp == 'A': #rock -- paper
                    score += 2
                elif opp == 'B': #paper -- scissors
                    score += 3
                else: #scissors -- rock
                    score += 1
            return score

    
input = open("Day2_input.txt", 'r').read().split('\n')
# print(rock_paper_scissor(input))

# input = ['A Y', 'B X', 'C Z']
print(rock_paper_scissor(input))