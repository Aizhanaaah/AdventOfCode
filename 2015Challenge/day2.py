with open("giftsdim.txt") as f:
    line1 = []
    for line in f:
        result = list(map(int, line.strip().split('x')))
        l = result[0]
        w = result[1]
        h = result[2]
        result = 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])
        line1.append(result)
    print(sum(line1))