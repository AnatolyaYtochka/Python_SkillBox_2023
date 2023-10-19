s = [int(i) for i in input().split()]
flag = False
if s.count(s[0]) == len(s):
    print('Все числа равны')
else:
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                flag = True
                break
    print('Есть равные и неравные числа' if flag else 'Все числа разные')