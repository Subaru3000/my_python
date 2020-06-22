import pandas as pd
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

print("Задание 1: Средний возраст футболистов: ", round(football['Age'].mean()))

print("Задание 2: Количество хладнокровных футболистов: ", football['Composure'].count())

print("Задание 3: Стандартное отклонение: ", round(football['ShortPassing'].std(), 2)) # sqrt(mean(x - x.mean())**2) - std

print("Задание 4: Сумма заработных плат за год: ", football['Wage'].sum())

print("Задание 5: Минимальная стоимость футболиста: ", football['Value'].min())

print("Задание 1: Средняя скорость с зарплатой выше среднего: ", round(football[football.Wage > football.Wage.mean()].SprintSpeed.mean(), 2))
#среди тех у кого зп выше среднего выбираем среднее значение и округляем до двух знаков

print("Задание 2: Средняя скорость с зарплатой ниже среднего: ", round(football[football.Wage < football.Wage.mean()].SprintSpeed.mean(), 2))

print("Задание 3: Позиция игрока с макс зарплатой: ", football[football.Wage == football.Wage.max()]['Position'][0])
#отбираем игрока с макс зп и находим его позицию

print("Задание 4: Количество пенальти, которые сделали бразильские футболисты: ", football[football.Nationality == 'Brazil'].Penalties.sum())

print("Задание 5: Средний возраст игроков с точностью удара головой больше 50: ", round(football[football.HeadingAccuracy > 50]['Age'].mean(), 2))

print("Задание 6: Возраст самого молодого игрока с хладнокровием и реакцией выше 90% от макс знач: ", football[(football.Composure > football.Composure.max() * 0.9) & (football.Reactions > football.Reactions.max() * 0.9)]['Age'].min())

print("Задание 7: Разница в реакции самых старых и самых молодых игроков: ", round(football[football['Age'] == football['Age'].max()]['Reactions'].mean() - football[football['Age'] == football['Age'].min()]['Reactions'].mean(), 2))

x = football[football['Value'] > football['Value'].mean()]['Nationality']
from statistics import mode
def most_common(List):
    return (mode(List))
List = sorted(x)
print("Задание 8: Страна с макс игроками, чья стоимость превышает среднее значение:", most_common(List))


print("Задание 9: Отношение зарплат у голкиперов с лучшими рефлексами и с лушим владением мячом: ", round(football[(football['Position'] == 'GK') & (football['GKReflexes'] == football['GKReflexes'].max())]['Wage'].mean() /football[(football['Position'] == 'GK') & (football['GKHandling'] == football['GKHandling'].max())]['Wage'].mean(), 2))

print("Задание 10: Отношение силы ударов наиболее и наименее агрессивных игроков: ", round(football[football['Aggression'] == football['Aggression'].max()]['ShotPower'].sum() / football[football['Aggression'] == football['Aggression'].min()]['ShotPower'].sum(), 2))