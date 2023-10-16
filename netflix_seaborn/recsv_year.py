import pandas as pd

# Загрузите CSV файл в DataFrame
df = pd.read_csv('Netflix.csv', encoding='latin1')

# Разбейте столбец Premiere на три отдельных столбца: месяц, день и год
df[['Month', 'Day', 'Year']] = df['Premiere'].str.split(' ', expand=True)

# Замените столбец Premiere столбцом Year
df['Premiere'] = df['Year']

# Удалите столбцы Month, Day и Year, если они больше не нужны
df.drop(['Month', 'Day', 'Year'], axis=1, inplace=True)

# Сохраните DataFrame обратно в CSV файл
df.to_csv('Netflix.csv', index=False)
