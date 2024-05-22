import pandas as pd

# Работа с набором данных

df = pd.read_csv('netflix.csv')

print("---------- Датасет Netflix: первые 5 строк данных ----------")
print(df.head())
print("\n---------- Датасет Netflix: информация о данных ----------")
print(df.info())
print("\n---------- Датасет Netflix: статистическое описание ----------")
print(df.describe())

# Определить среднюю зарплату по городам

df = pd.read_csv('dz.csv')

average_salary = df.groupby('City')['Salary'].mean()
print(f"---------- Средняя зарплата по городам ----------\n{average_salary}")
