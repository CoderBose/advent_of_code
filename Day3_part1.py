def calculatePriority(rucksack):
    i = 0
    j = len(rucksack)
    mid = (i + j) // 2
    rucksack1 = rucksack[i : mid]
    rucksack2 = rucksack[mid : j]

    hashMap1 = {}
    hashMap2 = {}

    for c in rucksack1:
        hashMap1[c] = 1 + hashMap1.get(c, 0)


    for c in rucksack2:
        hashMap2[c] = 1 + hashMap2.get(c, 0)


    priority = ''
    # Find the common keys
    common_keys = set(hashMap1.keys()) & set(hashMap2.keys())
    print(" 1: ", common_keys)
    common_key = common_keys.pop()
    
    # if common_keys:
    #     common_key = common_keys.pop()
    #     print(" 2: ", common_key)
    #     # Check if the common key appears at least once in both dictionaries
    #     if hashMap1.get(common_key, 0) >= 1 and hashMap2.get(common_key, 0) >= 1:
    #         priority = common_key
    #         print(" 3: ", priority)

    return checkPriority(common_key)
    
     

def checkPriority(priority):
    mapLower = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
    mapUpper = {'A' : 27, 'B' : 28, 'C' : 29, 'D' : 30, 'E' : 31, 'F' : 32, 'G' : 33, 'H' : 34, 'I' : 35, 'J' : 36, 'K' : 37, 'L' : 38, 'M' : 39, 'N' : 40, 'O' : 41, 'P' : 42, 'Q' : 43, 'R' : 44, 'S' : 45, 'T' : 46, 'U' : 47, 'V' : 48, 'W' : 49, 'X' : 50, 'Y' : 51, 'Z' : 52}
    if ord(priority) >= 65 and ord(priority) <= 90:
        return mapUpper[priority]
    return mapLower[priority]
    
input = open('Day3_input.txt', 'r').read().split('\n')
sum = 0
for i in input:
    sum += calculatePriority(i)
print(sum)

# sum = 0
# input = 'PPWvWQjPhrPQwlMWJJdMDGbJTdCJ'
# sum += calculatePriority(input)
# print(sum)
