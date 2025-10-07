with open("input.txt", "r", encoding="utf-8") as file:
    niceStringSum = 0
    
    vowelSet = {"a", "e", "i", "o", "u"}
    for line in file:
        print(line.strip())
        if sum(line.count(vowel) for vowel in vowelSet) >= 3 and 'ab' not in line and 'cd' not in line and 'pq' not in line and 'xy' not in line and any(line[i] == line[i + 1] for i in range(len(line) - 1)):
            print("nice")
            niceStringSum += 1
    print(niceStringSum)


with open("input.txt", "r", encoding="utf-8") as file:
    niceStringSum = 0
    for line in file:
        print(line.strip())
        if any(line[i:i+2] in line[i+2:] for i in range(len(line)-2)) and any(line[i] == line[i+2] for i in range(len(line)-2)):
            print("nice")
            niceStringSum += 1
    print(niceStringSum)
