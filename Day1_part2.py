def maxEnergyOfElf(input):
    maxCal = []
    cal = 0

    for i in input:
        if i == "":
            maxCal.append(cal)
            cal = 0
        else:
            cal += int(i)
        
    maxCal.sort()
    sum = maxCal[-1] + maxCal[-2] + maxCal[-3]
    print(sum)

input=open('Day1_input.txt', 'r').read().split('\n')
maxEnergyOfElf(input)