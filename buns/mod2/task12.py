string = input()
number = '+'
for i in string:
    if i.isdigit():
        number += i
print(number)