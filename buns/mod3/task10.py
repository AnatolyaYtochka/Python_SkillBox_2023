size = int(input())
for i in range(1 , size + 1):
    for j in range(1, size + 1):
        print(str(j), end=', ' if j != size else '\n')
print()
for i in range(1 , size + 1):
    for j in range(1, size + 1):
        print(i, end=', ' if j != size else '\n')