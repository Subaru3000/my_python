
print("Задание 1: Строка 'May 9 2017 9:00AM' в формате datetime: ")
from datetime import datetime, timedelta
dateString = 'May 9 2017 9:00AM'
date = datetime.strptime(dateString, '%b %d %Y %I:%M%p')
print(date)
date.hour



print("Задание 2: Прибавляем час к 'May 9 2017 9:00AM' ")
date += timedelta(hours=1)
date



dateString1 = date.strftime('%Y-%m-%d')
print("Задание 3: Записываем  результат предыдущего задания в формате '%Y-%m-%d'", dateString1)




print("Задание 4:")
spisok=[]
start = '2018-01-01'
end = '2018-01-03'
startDate = datetime.strptime(start, '%Y-%m-%d')
endDate = datetime.strptime(end, '%Y-%m-%d')
day = startDate
day = startDate
while day <= endDate:
    spisok.append(day.strftime('%Y-%m-%d %H:%M:%S'))
    day += timedelta(hours=1)
print('Последним значением для 2 января будет: ',spisok[47])

from datetime import datetime
import pandas as pd
import time
data = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data.tsv', sep='\t')

def convert_to_datetime(row):
    return datetime.strptime(row['date'], '%d.%m.%Y %H:%M')
def make_unix_time(row):
    return time.mktime(row['datetime'].timetuple())
data['datetime'] = data.apply(convert_to_datetime, axis=1)
data['unixtime'] = data.apply(make_unix_time, axis=1)
groupping = data.groupby(["user_id"]).agg(["min","max"]).unixtime
def v(row):
    return row['max'] - row['min']
groupping['diff'] = groupping .apply(v, axis = 1)
groupping = groupping[groupping['diff'] != 0]
days = round(groupping["diff"].mean() / 86400,1)
print("Задание:\n Среднее значение столбца diff после фильтрации в секундах: ", groupping["diff"].mean())
print("Количество дней: ", days)