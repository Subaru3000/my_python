# самые частые контрольные

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

print(sorted(kr.cd_type_name))

ww = sorted(kr.cd_type_name)
from statistics import mode
def most_common(List):
    return (mode(List))
print('Ответ: ', most_common(ww))