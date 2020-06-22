import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

print("Количество футбольных клубов: ", football['Club'].nunique())

print("Клуб с наименьшим количеством игроков:\n ", football['Club'].value_counts()[football['Club'].value_counts() == football['Club'].value_counts().min()])

print("Позиции игроков, занимающих менее 1%:\n", football['Position'].value_counts(normalize = True)[football['Position'].value_counts(normalize = True) < 0.01])

print("Пределы худших 20% показателей точности ударов ногой: ", football['FKAccuracy'].value_counts(bins = 5).sort_index().index[0])

print("Показатели ударов ногой большинства футболистов: ", football['FKAccuracy'].value_counts(bins=5).index[0])

print("Задача 1: Количество испанцев с зарплатой не более четверти от максимальной: ", football[football['Wage'] <= football[football['Nationality'] == 'Spain']['Wage'].value_counts(bins=4).index[0].right]['Wage'].count())

print("Задача 2: Количество различных национальностей в Manchester United:", len(football[football['Club'] == 'Manchester United']['Nationality'].unique()))

print("Задача 3: Бразильцы, играющие в Juventus: ", football[(football['Club'] == 'Juventus') & (football['Nationality'] == 'Brazil')]['Name'].unique())

footballPlayers = 0
club = ''
for clubb in football['Club'].unique():
    if football[(football['Club'] == clubb) & (football['Age'] > 35)]['Name'].count() > footballPlayers:
        footbalPlayers = football[(football['Club'] == club) & (football['Age'] > 35)]['Name'].count()
        club = clubb
print("Задача 4: Клуб с наибольшим числом игроков старше 35 лет: ", club)

print("Задача 5: Количество старейших аргентинцев-футболистов: ", football[(football['Nationality'] == 'Argentina') & (football['Age'] >= football['Age'].value_counts(bins=4).index[3].left)]['Age'].count())

print("Задача 6: Процент футболистов, которым 21 год, от всего испанского состава: ", round(football[football['Nationality'] == 'Spain']['Age'].value_counts(normalize=True)[21], 2))

