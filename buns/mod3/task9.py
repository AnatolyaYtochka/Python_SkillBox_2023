def makeSteps(n):
    x, y = 0, 0
    dx, dy = 1, 1
    steps, stepForSide = 0, 1
    for i in range(n):
        dx = -dx
        for j in range(stepForSide):
            x += dx
            steps += 1
            if steps >= n:
                return str(x) + ' ' + str(y)
        
        dy = -dy
        for j in range(stepForSide):
            y += dy
            steps += 1
            if steps >= n:
                return str(x) + ' ' + str(y)
            
        stepForSide += 1
    return str(x) + ' ' + str(y)

n = int(open('input.txt').readline())
print(makeSteps(n))
