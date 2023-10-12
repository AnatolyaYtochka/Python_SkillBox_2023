def checkWinner(positions, winner):
    k = len(positions)
    for i in range(k):
        summ = 0
        for j in range(k):
            if positions[i][j] == winner:
                summ += 1
        if summ == k:
            return True;
        
    for i in range(k):
        summ = 0
        for j in range(k):
            if positions[j][i] == winner:
                summ += 1
        if summ == k:
            return True;
    
    summ = 0    
    for i in range(k):
        for j in range(k):
            if positions[i][j] == winner and i == j:
                summ += 1
        if summ == k:
            return True;
                
    return False;

s = input()
playingField = []
playingField.append(s)
for i in range(len(s) - 1):
    playingField.append(input())
positions = [[j for j in i] for i in playingField]


isXWinner = checkWinner(positions, 'X')
isOWinner = checkWinner(positions, 'O')
if isXWinner == isOWinner:
    print('Ничья')
elif isOWinner:
    print('O')
else:
    print('X')

    
    

