def maxEnergyOfElf(input):
    maxCal = 0
    cal = 0

    for i in input:
        if i == "":
            cal = 0
        else:
            cal += int(i)
            if cal > maxCal:
                maxCal = cal
    
    return maxCal

    # energy = input.split("")
    # maxCal = 0
    # cal = 0
    # for en in energy:
    #     cal += int(en)
    #     if cal > maxCal:
    #         maxCal = cal
    # return maxCal

input=open('Day1_input.txt', 'r').read().split('\n')
# input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
print(maxEnergyOfElf(input))