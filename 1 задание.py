import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()


x = ege['stud_kod']
y = kr['stud_kod']

def ff(l): #deleteduplicates
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

print(len(ff(sorted(x))))
print(len(ff(sorted(y))))
print("1 задание. Ответ:", len(ff(sorted(x))), len(ff(sorted(y))))