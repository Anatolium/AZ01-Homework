import pandas as pd

# df = pd.read_csv('hh.csv')

# df['Test'] = [new for new in range(29)]
# print(df)
#
# df.drop('Test', axis=1, inplace=True)
# print(df)
#
# df.drop(28, axis=0, inplace=True)
# print(df)

df = pd.read_csv('animal.csv')
print(df)

# df = df.fillna(0, inplace=False)
# print(df)

# df = df.dropna(inplace=False)
# print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)
