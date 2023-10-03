def transferToAnotherNumberSystem(number, basis):
    digits = '0123456789ABCDEF'
    newNumber = ''
    while number > 0:
        newNumber += digits[number % basis]
        number //= basis
    return newNumber[::-1]
        

a = int(input())
binNumber = transferToAnotherNumberSystem(a, 2)
octNumber = transferToAnotherNumberSystem(a, 8)
hexNumber = transferToAnotherNumberSystem(a, 16)
print(binNumber, octNumber, hexNumber)
