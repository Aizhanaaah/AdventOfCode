with open("floors.txt") as f:
    floor = 0
    for i in f.read():
        if i == '(':
            floor += 1
        else:
            floor -= 1
print(floor)
