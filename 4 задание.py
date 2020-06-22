#будем рассматривать условие задачи в концепции среднего показателя всех рез егэ по всем предметам в конкретном году, тем самым уточнив условие

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

qq = sorted(ege.year)
print(qq)
print(ege[ege.year == 2013].ball.mean())

def ff(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

print(ff(qq))

def gg(x):
    toto = ege[ege.year == x].ball.mean()
    return toto


print(list(map(gg, ff(qq))))