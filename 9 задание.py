import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

def qq(x):
    if type(x) == str:
        return '0'
    else:
        return x


x = sorted(kr.predmet_name)

def ff(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

print(ff(x))
s = ff(x)

xx = float(input("Выберете id студента: "))


def abc(qqqq):
    c = kr[kr.stud_kod == xx]
    d = c[c.predmet_name == qqqq].ball

    cc = sorted(d, key=qq(str))
    qwe = []
    for i in range(0, len(cc)):
        if type(cc[i]) != str:
            qwe.append('0')
        else:
            qwe.append(cc[i])
    dd = [float(i.replace(',', '.')) for i in qwe]  #список баллов по предмету у отдельного студента по окончании обучения
    return sum(dd) / len(dd)


rrr =list(map(abc, s))
print(rrr)

