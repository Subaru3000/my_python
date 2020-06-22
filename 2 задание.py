import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

x = ege['predmet_name']


from statistics import mode
def most_common(List):
    return (mode(List))
List = sorted(x)
print(List)
print(most_common(List))
# самый cдаваемый предмет

def ff(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

print(ff(sorted(ege['stud_kod'])))
qq = ff(sorted(ege['stud_kod']))
def gg(kod):
    xx = ege[ege.stud_kod == kod].predmet_name
    return sorted(xx)


print(list(map(gg, qq)))

ww = list(map(gg, qq))
ee = list(map(tuple, ww))
print(ee)
def most_commonn(lst):
    res = dict((lst.count(i), i) for i in set(lst))
    return res[max(res.keys())]

print(most_commonn(ee))
# если в условии подразумевается набор предметов