def calculatePriority(group):
    rucksack1 = group[0]
    rucksack2 = group[1]
    rucksack3 = group[2]

    hashMap1 = {}
    hashMap2 = {}
    hashMap3 = {}

    for c in rucksack1:
        hashMap1[c] = 1 + hashMap1.get(c, 0)

    for c in rucksack2:
        hashMap2[c] = 1 + hashMap2.get(c, 0)
    
    for c in rucksack3:
        hashMap3[c] = 1 + hashMap3.get(c, 0)

    priority = ''
    # Find the common keys
    common_keys = set(hashMap1.keys()) & set(hashMap2.keys()) & set(hashMap3.keys())
    common_key = common_keys.pop()
    val = checkPriority(common_key)
    return val

    # if common_keys:
    #     common_key = common_keys.pop()
    #     # Check if the common key appears at least once in all three dictionaries
    #     if hashMap1.get(common_key, 0) >= 1 and hashMap2.get(common_key, 0) >= 1 and hashMap3.get(common_key, 0) >= 1:
    #         priority = common_key
    # val = checkPriority(priority)
    # return val

def checkPriority(priority):
    mapLower = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
    mapUpper = {'A' : 27, 'B' : 28, 'C' : 29, 'D' : 30, 'E' : 31, 'F' : 32, 'G' : 33, 'H' : 34, 'I' : 35, 'J' : 36, 'K' : 37, 'L' : 38, 'M' : 39, 'N' : 40, 'O' : 41, 'P' : 42, 'Q' : 43, 'R' : 44, 'S' : 45, 'T' : 46, 'U' : 47, 'V' : 48, 'W' : 49, 'X' : 50, 'Y' : 51, 'Z' : 52}
    if ord(priority) >= 65 and ord(priority) <= 90:
        return mapUpper[priority]
    return mapLower[priority]
    
input = open('Day3_input.txt', 'r').read().split('\n')
# to create a subarray with 3 words together for the entire input
subList = [input[n:n+3] for n in range(0, len(input), 3)]
sum = 0
for i in range(len(subList)):
    sum += calculatePriority(subList[i])

print(sum)

# sum = 0
# input = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'
# sum += calculatePriority(input.split('\n'))
# print(sum)
