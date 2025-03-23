list1values = input()
list1Values1 = list(map(int, list1values.split()))
list2values = input()
list2Values2 = list(map(int, list2values.split()))
sorted1 = sorted(list1Values1)
sorted2 = sorted(list2Values2)
distance = []
for i, j in zip(sorted1, sorted2):
    distance.append(abs(j-i))
totalSum = sum(distance)
print(totalSum)

