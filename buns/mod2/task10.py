string = input() + ' '
newString = ''
for i in range(len(string) - 1):
    if string[i + 1]  == ' ':
        newString += string[i]
print(newString)
    