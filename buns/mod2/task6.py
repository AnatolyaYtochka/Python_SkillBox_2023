def getFragment(siteName):
    string = ''
    startIndex = 0
    while siteName[startIndex] != '.':
        string += siteName[startIndex]
        startIndex += 1
    return string

siteName = input() + '.'
a = getFragment(siteName)
siteName = siteName[len(a) + 1::]
b = getFragment(siteName)
siteName = siteName[len(b) + 1::]
c = getFragment(siteName)
print(c)
print(b)
print(a)
