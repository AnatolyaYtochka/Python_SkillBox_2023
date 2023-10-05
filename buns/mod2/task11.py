string = input().replace(' ', '')
flag = False
for i in range(0, len(string) - 1):
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            flag = True
            break
print(flag)
    

    
