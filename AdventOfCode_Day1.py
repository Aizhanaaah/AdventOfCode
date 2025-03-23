#3rd solution:
'''
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
'''



#2nd solution:
'''
left_value = []
right_value = []

try:
    while True:
        line = input().strip()
        if not line:
            break
        left, right = map(int, line.split())
        left_value.append(left)
        right_value.append(right)
except EOFError:
    pass
sorted1 = sorted(left_value)
sorted2 = sorted(right_value)
distance = []
for i, j in zip(sorted1, sorted2):
    distance.append(j-i)
totalSum = sum(distance)
print(totalSum)
'''

#3rd solution that works:

data = [*map(int, open('input1.txt').read().split())]
A, B = sorted(data[0::2]), sorted(data[1::2])
print(sum(map(lambda a, b: abs(a-b), A, B)))

#partB:
frequency_counter = Counter(A)
list = []
for j in B:
    if j in frequency_counter:
        list.append(j * frequency_counter[j])
print(sum(list))
