string = input()
summOfEven = 0
summOfOdd = 0
for i in range(0, len(string)):
    if i % 2 == 0:
        summOfEven += int(string[i])
    else:
        summOfOdd += int(string[i])
if (summOfEven + 3 * summOfOdd) % 10 == 0:
    print('yes')
else:
    print('no')
    