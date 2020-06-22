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



def qq(x):
    if type(x) == str:
        return '0'
    else:
        return x



def aaa(xxx): #возвращает общий средний балл всех студентов за дисциплину
    cc = sorted(kr[kr.predmet_name == xxx].ball, key=qq(str))
    qwe = []
    for i in range(0, len(cc)):
        if type(cc[i]) != str:
            qwe.append('0')
        else:
            qwe.append(cc[i])
    eee = [float(i.replace(',', '.')) for i in qwe]
    return sum(eee)/len(eee)

print(aaa('Автоматизированные системы обработки учетной информации'))
print(aaa(s[2]))


ddd = list(map(aaa, s))
sd = sorted(ddd)[:5]
print(sd)

qee=[]
for i in range(0, len(s)):
    if sd.count(aaa(s[i]))>0:
        qee.append(s[i])

print(qee)
