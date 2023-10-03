def getNumbers(numbers):
    number = ''
    startIndex = 0
    while numbers[startIndex] != ' ':
        number +=  numbers[startIndex]
        startIndex += 1
    return int(number)

numbers = input() + ' '
a = getNumbers(numbers)
numbers = numbers[len(str(a)) + 1::]
b = getNumbers(numbers)
numbers = numbers[len(str(b)) + 1::]
c = getNumbers(numbers)
middleNumber = a + b + c - max(a, b, c) - min(a, b, c)
print(middleNumber)
