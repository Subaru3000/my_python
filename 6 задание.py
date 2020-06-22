import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

print(kr)

x = sorted(kr.predmet_name)

def ff(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n
print(ff(x))
s = ff(x)#список всех предметов

def aaa(xxx):
    qqq = sorted(kr[kr.predmet_name == xxx].ball)
    eee = [float(i.replace(',', '.')) for i in qqq]
    return sum(eee)/len(eee)

print(aaa('Автоматизированные системы обработки учетной информации'))
print(kr[kr.predmet_name == s[2]])
print(aaa(s[0]))


for i in range(0, len(s)):
    print(aaa(s[i]))
