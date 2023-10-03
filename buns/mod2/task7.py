string = input()
count0, count1 = 0, 0
for i in string:
    if i == '0':
        count0 += 1
    else:
        count1 += 1
if count0 == count1:
    print('yes')
else:
    print('no')
