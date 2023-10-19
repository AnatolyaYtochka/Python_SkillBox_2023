def findNOD(a, b):
    if a == 0:
        return b
    return findNOD(b % a, a)

a, b = int(input()), int(input())
print(findNOD(a, b))