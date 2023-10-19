string = input()
dict = {}
for i in string:
    if i in dict:
        continue
    else:
        dict[i] = string.count(i)
count = 0
for i in dict:
    if dict.get(i) % 2 != 0:
        count += 1
halfPalindrom = ''
center = ''
if (count == 1 or count == 0):
    for i in dict:
        n = dict.get(i)
        if n % 2 == 0 or n > 1:
            halfPalindrom += i * (n // 2)
        if n % 2 == 1:
            center = i      
    print('Можно составить палиндром! Вот он:  ' + halfPalindrom + center + halfPalindrom[::-1])
else:
    print('Нельзя составить палиндром:(')