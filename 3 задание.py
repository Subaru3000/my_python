import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ege.csv"
ege = pd.read_csv(url, sep=';')
ege.head()

import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stud/stud_spisok_ball.csv"
kr = pd.read_csv(url, sep=';')
kr.head()

xx = input("Выберете предмет: ")


print('Out: ')
print(ege[ege.predmet_name == xx].ball.min())
print(ege[ege.predmet_name == xx].ball.mean())
print(ege[ege.predmet_name == xx].ball.max())