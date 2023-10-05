def getFragment(originalString):
    string = ''
    startIndex = 0
    while originalString[startIndex] != ',':
        string += originalString[startIndex]
        startIndex += 1
    return string

originalString = input() + ','
originalString = originalString.replace(' ', '')
string = getFragment(originalString)
originalString = originalString[len(string) + 1::]
symbol = getFragment(originalString)

count = 0
while string[count] == symbol:
    count += 1
print(count)
