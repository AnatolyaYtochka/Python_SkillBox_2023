def getNumbers(numbers):
    number = ''
    startIndex = 0
    while numbers[startIndex] != ',':
        number +=  numbers[startIndex]
        startIndex += 1
    return int(number)

numbers = input() + ','
numbers = numbers.replace(' ', '')
a = getNumbers(numbers)
numbers = numbers[len(str(a)) + 1::]
b = getNumbers(numbers)
c = a % b
print(c)
