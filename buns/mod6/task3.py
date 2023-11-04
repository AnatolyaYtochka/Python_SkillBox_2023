def armstrongNumbersGenerator():
    n = 10
    while True:
        digits = [int(i) for i in str(n)]
        k = len(digits)
        if sum([i ** k for i in digits]) == n:
            yield n
        n += 1

gen = armstrongNumbersGenerator()

def getNumbers():
    return next(gen)

for i in range(8):
    print(getNumbers(), end=' ')