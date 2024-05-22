import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}
df = pd.DataFrame(data)
print(df)

df.to_csv('output.csv', index=False)


# df = pd.read_csv('World-happiness-report-2024.csv')
#
# print(df.head())
# print(df.tail())
#
# # info(): сколько всего данных в датасете, названия всех столбцов, какое число столбцов содержит информацию,
# # тип хранящихся данных, сколько памяти тратится
# print(df.info())
#
# # describe(): статистические данные – найти минимальные, максимальные и средние значения, количество и тд
# print(df.describe())
#
# # Сведения из определённого столбца
# print(df['Country name'])
#
# # Чтобы вывести одновременно несколько столбцов, нужно их названия заключить в двойные квадратные скобки
# print(df[['Country name', 'Regional indicator']])
#
# # Вывести не весь столбец, а определённую строку: надо использовать функцию loc и указать индекс строки
# print(df.loc[56])
#
# # Вывести определённую строку и определённый столбец
# print(df.loc[56, 'Healthy life expectancy'])
#
# # Фильтрация данных:
# print(df[df['Healthy life expectancy'] > 0.7])

