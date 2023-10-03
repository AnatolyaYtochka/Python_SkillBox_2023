symbol = ord(input())
shift = int(input())
newSymbol = symbol + shift
if newSymbol > 122:
    newSymbol = newSymbol % 122 + 96
elif newSymbol < 97:
    newSymbol = 122 - (96 - newSymbol)
print(chr(newSymbol))
