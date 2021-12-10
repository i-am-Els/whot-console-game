listA = [12, 21, 9, 13, 9]

small = listA[0]
j = len(listA)
for l in range(1, j):
    if small > listA[l]:
        small = listA[l]

print(listA.index(small))
print(small)