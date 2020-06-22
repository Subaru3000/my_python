import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/it.csv')


wage = df[df['З/п в валюте найма'].str.contains('₽')]
meanWage = wage['З/п в валюте найма'].str.translate(str.maketrans({'₽': '', ',': '.', '\xa0': ''})).astype(float).mean()
print('Средняя зарплата по данным в рублях: ', meanWage)


print("Технология с максимальной зарплатой по данным в рублях: ", wage.groupby(['Технология'])['З/п в валюте найма'].max().sort_values(ascending=False).index[0])


print('Возраст програмистов с макисмальной зарплатой: ', wage.groupby(['Дата рождения'])['З/п в валюте найма'].max().sort_values(ascending=False).index[0])


print("Зарплаты работников, у которых в названии вакансии встречается слово Engineer", df[df['Вакансия'].str.contains('Engineer')][['Вакансия','З/п в валюте найма']])
