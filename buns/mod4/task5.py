file = open('input.txt')
s = ''.join(file)
dict = {}
for i in s:
    if i.isalpha():
        if i in dict:
            continue
        else:
            dict[i] = s.count(i)
sortedDict = sorted(dict.items(), key=lambda dict: dict[1])
statistic = ''
for i in range(len(sortedDict)):
    statistic += sortedDict[i][0] + ': ' + str(sortedDict[i][1]) + '\n'
newFile = open('statistic.txt', 'w+')
newFile.write(statistic)
newFile.close()