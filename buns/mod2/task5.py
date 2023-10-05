def getFragment(originalString):
    string = ''
    startIndex = 0
    while originalString[startIndex] != ',':
        string += originalString[startIndex]
        startIndex += 1
    return string

originalString = input() + ','
originalString = originalString.replace(' ', '')
symbol = ord(getFragment(originalString))
originalString = originalString[2::]
shift = int(getFragment(originalString))

newSymbol = symbol + shift
if newSymbol > 122:
    newSymbol = newSymbol % 122 + 96
elif newSymbol < 97:
    newSymbol = 122 - (96 - newSymbol)
print(chr(newSymbol))
