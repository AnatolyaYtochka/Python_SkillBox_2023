consonantLetters = 'бвгджзйклмнпрстфхцчшщ'
vowelLetters = 'аеёиоуыэюя'
string = input()
vowelLettersCount = 0
consonantLettersCount = 0
for i in string:
    if i in vowelLetters:
        vowelLettersCount += 1
    elif i in consonantLetters:
        consonantLettersCount += 1
print(vowelLettersCount, consonantLettersCount)