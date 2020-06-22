import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

a = sorted(kr.stud_kod)
sorted(kr.stud_kod)
def ff(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def qq(x):
    if type(x) == str:
        return '0'
    else:
        return x


b = ff(a)
print(b)

def rrr(x):
    cc = sorted(kr[kr.stud_kod == x].ball, key=qq(str))
    qwe=[]
    for i in range(0, len(cc)):
        if type(cc[i]) != str:
            qwe.append('0')
        else:
            qwe.append(cc[i])

    d = [float(i.replace(',', '.')) for i in qwe]
    return sum(d)/len(d)


rrr(9)
print(list(map(rrr, b)))
lll = list(map(rrr, b))
print(sorted(lll))
hh = sorted(lll)[:3]
print(hh)

ss=[]
for i in range(0, len(b)):
    if hh.count(rrr(b[i]))>0:
        ss.append(b[i])

print(ss)