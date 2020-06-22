import inline as inline
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/vkontakte_group_01_2016-08-01_2020-03-15.csv")
dfc= pd.get_dummies(df, columns=['Критерий'])
def to_datetime(row):
    return datetime.strptime(row['Дата'], '%d.%m.%Y')


p = dfc[['Дата', 'Значение']][dfc['Критерий_views'] == 1]
p['Дата'] = p.apply(to_datetime, axis=1).dt.strftime('%Y')
py = p.groupby(['Дата'])['Значение'].sum()
print("Задание 1: Статистика посещения группы\n",py)




import pylab
a = dfc[['Дата','Значение']][dfc['Критерий_reach'] == 1]
a['Дата'] = a.apply(to_datetime, axis=1).dt.strftime('%Y-%m')
au = a.groupby(['Дата'])['Значение'].sum()
f = dfc[['Дата','Значение']][dfc['Критерий_reach_subscribers'] == 1]
f['Дата'] = f.apply(to_datetime, axis=1).dt.strftime('%Y-%m')
fo = f.groupby(['Дата'])['Значение'].sum()
plt.title('Суммарный анализ охвата')
plt.xlabel('Дата')
plt.ylabel('Значение')
au.plot(label="reach", linestyle='--',color = 'orange')
fo.plot(label = "reach_subscribers", linestyle='--',color = 'red')
pylab.ylim(0, 9000)
plt.legend(loc="upper left")
plt.grid(True)
plt.show()


gender = dfc[['Дата', 'Значение','Парам. №1']][dfc['Критерий_gender'] == 1]
gender1 = gender.groupby(['Парам. №1'])['Значение'].sum()
print("Задание 3: Провести анализ демографии по полу:\n",gender1 )



age = dfc[['Парам. №1', 'Значение']][dfc['Критерий_age'] == 1]
age1 = age.groupby(['Парам. №1'])['Значение'].sum()
print("Задание 3: Провести анализ демографии по возрасту аудитории:\n",age1 )


country = dfc[['Парам. №1','Значение']][dfc['Критерий_countries'] == 1]
country1 = country.groupby(['Парам. №1'])['Значение'].sum()
print("Задание 3: Провести анализ демографии по стране:\n",country1 )



get_feedback = dfc[['Дата','Парам. №1','Значение']][dfc['Критерий_feedback'] == 1]
get_feedback['Дата'] = get_feedback.apply(to_datetime, axis=1).dt.strftime('%Y-%m')
print(get_feedback['Парам. №1'].value_counts())



like = get_feedback[get_feedback['Парам. №1'] == 'Нравится'].groupby(['Дата'])['Значение'].sum().plot(label="лайки", linestyle='--',color = 'orange')
comment = get_feedback[get_feedback['Парам. №1'] == 'Комментарии'].groupby(['Дата'])['Значение'].sum().plot(label="комментарии", linestyle='--',color = 'red')
repost = get_feedback[get_feedback['Парам. №1'] == 'Рассказали друзьям'].groupby(['Дата'])['Значение'].sum().plot(label="репосты", linestyle='--',color = 'yellow')
plt.legend(loc="upper left")
plt.grid(True)
plt.show()


print('Задание 5: Наиболее популярна группа для людей в возрасте: ',str(age1.sort_values(ascending=False).index[1]) , 'лет и', str(age1.sort_values(ascending=False).index[0]), 'лет')
print('Задание 5: Наиболее популярна группа для людей, которые живут в: ', str(country1.sort_values(ascending=False).index[0]))


print("Задание 5: Проведя анализ мы узнали, что по возрастному и демографическому показателям группа пользуется популярностью среди активных пользователей из России моложе 30 лет, исходя из этого мы можем сделать вывод, что группа подходит для продвижения нового товара")
