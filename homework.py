import pandas as pd

# Работа с набором данных

print("------------ Задача 1 ------------")
df = pd.read_csv('netflix.csv')

print("----- Датасет Netflix: первые 5 строк данных -----")
print(df.head())
print("\n----- Датасет Netflix: информация о данных -----")
print(df.info())
print("\n----- Датасет Netflix: статистическое описание -----")
print(df.describe())

# Определить среднюю зарплату по городам

print("\n------------ Задача 2 ------------")
df = pd.read_csv('dz.csv')

print(df)
print()
group = df.groupby('City')['Salary'].mean()
print(f"----- Средняя зарплата по городам -----\n{group}")
