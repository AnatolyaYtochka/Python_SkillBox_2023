def getPower(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return getPower(a**2, n / 2)
    return a * getPower(a, n - 1)

a, n = int(input()), int(input())
print(getPower(a, n))