#part A:

with open("floors.txt") as f:
    floor = 0
    for i in f.read():
        if i == '(':
            floor += 1
        else:
            floor -= 1
print(floor)


#part B:

with open("floors.txt") as f:
    floor = 0
    position = 0
    for i in f.read():
        if i == '(':
            floor += 1
            position += 1
        else:
            floor -= 1
            position += 1
        if floor == -1:
            break
print(position)
