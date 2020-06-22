
s = [1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4]

def ff(s):
    x = s[:5]
    mmax = sum(s[:5])
    qq = x
    for i in range(5, len(s)):
        x.pop(0)
        x.append(s[i])
        if sum(x) > mmax:
            mmax = sum(x)
            qq = i
    return s[qq-4:qq+1]



print(ff(s))

print(ff([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5]))