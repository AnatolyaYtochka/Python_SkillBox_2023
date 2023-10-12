s = input().split()
print(len([True for i in range(0, len(s) - 1) for j in range(i + 1, len(s)) if s[i] == s[j]]) != 0)
