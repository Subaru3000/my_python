
import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

print("Задание 1: Средняя запрплата на различных позициях: ", football.groupby(['Position']).mean()['Wage'].sort_values(ascending=False).index[0])

print("Задание 1: Средняя запрплата в различных клубах:\n ", football.groupby(['Club']).agg(['mean', 'median'])['Wage'])

same_club = []
for club in football['Club'].unique():
    if football[football['Club'] == club]['Wage'].mean() == football[football['Club'] == club]['Wage'].median():
        same_club.append(club)
        l = len(same_club)
print("Задание 1: Клубы с одинаковыми средней и медианной зарплатами:\n",same_club,"\n", "Их количество: ", l)

clubb = ''
wage = 0
same_club = []
for club in football['Club'].unique():
    if football[football['Club'] == club]['Wage'].mean() == football[football['Club'] == club]['Wage'].median():
        same_club.append(club)
        l = len(same_club)
        if football[football['Club'] == club]['Wage'].mean() > wage:
            wage = football[football['Club'] == club]['Wage'].mean()
            clubb = club
print('Задание 2: Максимальная средняя оплата равна: ', wage, 'в клубе', clubb)

print("Задача 1: Бюджет Chelsea: ", football.groupby(['Club']).sum().loc['Chelsea']['Wage'])

print("Задача 2: Максимальная зарплата футболиста из Аргентины в возрасте 20-ти лет:", football[(football['Nationality'] == 'Argentina') & (football['Age'] == 20)]['Wage'].max())

print("Задача 3: Максимальная зарплата футболиста из Аргентины в возрасте 30-ти лет:", football[(football['Nationality'] == 'Argentina') & (football['Age'] == 30)]['Wage'].max())

print("Задача 4: Минимальнаяя зарплата футболиста из Аргентины в возрасте 30-ти лет: ", football[(football['Nationality'] == 'Argentina') & (football['Age'] == 30)]['Wage'].min())

print("Задача 5: Максимальные сила и баланс игроков FC Barcelona: ", str(football[(football['Club'] == 'FC Barcelona') & (football['Nationality'] == 'Argentina')]['Strength'][0].max()),";",football[(football['Club'] == 'FC Barcelona') & (football['Nationality'] == 'Argentina')]['Balance'].max())
