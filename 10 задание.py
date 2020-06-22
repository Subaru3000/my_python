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

a = sorted(kr.semestr)
b = list(range(1, a[-1]+1))
print(b)
xx = input("Выберете id студента: ")


def res(x):
    def abc(qqqq):
        c = kr[kr.stud_kod == x]
        d = c[c.semestr == qqqq].ball

        cc = sorted(d, key=qq(str))
        qwe = []
        for i in range(0, len(cc)):
            if type(cc[i]) != str:
                qwe.append('0')
            else:
                qwe.append(cc[i])
        dd = [float(i.replace(',', '.')) for i in qwe]
        return sum(dd)/len(dd)
    rrr = list(map(abc, b))
    return rrr




out = res(float(xx))
print(out)

import matplotlib.pyplot as plt

x = tuple(range(1, 9))
y = tuple(out)
assert len(x) == len(y)

plt.plot(x, y)
plt.grid(True)
plt.show()