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