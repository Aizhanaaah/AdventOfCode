#Part A:


with open("locations.txt") as f:
    x = 0
    y = 0
    myset = set()
    myset.add((0, 0))
    for char in f.read():
        if char == '>':
            x += 1
        elif char == '<':
            x -= 1
        elif char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        myset.add((x, y))
    print(len(myset))


#    Part B:
with open("locations.txt") as f:
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    myset = set()
    myset.add((x, y))
    myset.add((x1, y1))
    text = f.read()
    for i in range(len(text)):
        char = text[i]
        if i % 2 == 0:
            if char == '>':
                x += 1
            elif char == '<':
                x -= 1
            elif char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            myset.add((x, y))
        else:
            if char == '>':
                x1 += 1
            elif char == '<':
                x1 -= 1
            elif char == '^':
                y1 += 1
            elif char == 'v':
                y1 -= 1
            myset.add((x1, y1))
    print(len(myset))
