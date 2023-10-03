string = input().replace(' ', '')
print(string)
flag = False
for i in range(0, len(string) - 1):
    print(string[i])
    for j in range(i + 1, len(string)):
        print(string[j])
        if string[i] == string[j]:
            flag = True
            break
print(flag)
    

    