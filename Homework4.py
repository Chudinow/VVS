import pandas as pd
import numpy as np

database = pd.read_csv('tested.csv')
#1.1
print(database.isnull().sum())
print("\n")
#1.2
print(database.info())
print("\n")
#1.3

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(database.head())
print("\n")
#1.4
print(database["Age"].mean())
print(database["Age"].max())
print(database["Age"].min())
print(database["Age"].median())
print(database["Age"].std())
print("\n")
#1.5
column_list = database.columns.tolist()
print(f'Колво заголовков - {len(column_list)}')
row_list = len(database)
print(f'Колво строк - {row_list}')

#2.1
print("\n")
#a
survival_by_sex = database.groupby('Sex')['Survived'].mean() * 100
print("процент выживших")
print(survival_by_sex)
print("\n")

#b
average_age_by_sex = database.groupby('Sex')['Age'].mean()
print("средний возраст")
print(average_age_by_sex)
print("\n")
#c
age_by_survival_sex = database.groupby(['Sex', 'Survived'])['Age'].mean()
print("средний возраст выживших и погибших")
print(age_by_survival_sex)
print("\n")

#2.2

#a
filter_2_2_a = database[(database['Age'] > 30) & (database['Sex'] == 'male') & (database['Pclass'] == 1)]
print("старше 30, мж, 1кл:")
print(f"колво пассажиров: {len(filter_2_2_a)}")
if len(filter_2_2_a) > 0:
    print(filter_2_2_a[['Name', 'Age', 'Sex', 'Pclass', 'Survived']].head())
print()

#b
filter_2_2_b = database[((database['Age'] < 18) or (database['Sex'] == 'female')) and (database['Survived'] == 1)]
print(" моложе 18 или женщины, выжили:")
print(f"колво пассажиров: {len(filter_2_2_b)}")
if len(filter_2_2_b) > 0:
    print(filter_2_2_b[['Name', 'Age', 'Sex', 'Survived']].head())
print()
#c
print(" группировка по классу и полу")
group_2_2_c = database.groupby(['Pclass', 'Sex']).agg({'Age': 'mean','Survived': 'mean','Fare': 'mean'}).round(2)
print(group_2_2_c)
