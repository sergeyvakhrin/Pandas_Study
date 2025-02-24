import json

import pandas as pd

reviews = pd.read_csv('titanic.csv', index_col=0)


# Задача 1. Расчет среднего возраста пассажиров по полу.
# Написать функцию, которая принимает на вход DataFrame из датасета "Titanic.csv".
# Функция должна вычислить средний возраст мужчин и женщин отдельно и вернуть результат
# в виде словаря в формате JSON.

#
# def foo(df):
#     """ Моё решение """
#     male_grouped = df.groupby('Sex')
#     mean_male = male_grouped.agg({'Age': 'mean'})
#     # json_str = mean_male.to_json(orient='records')
#     # json_obj = json.loads(json_str)
#
#     df_dict = mean_male.to_dict()
#     data = df_dict['Age']
#     return json.dumps(data)
#
#
# def avg_age_by_gender(df):
#     """ Решение предложенное на ресурсе """
#     avg_age_male = df[df['Sex'] == 'male']['Age'].mean()
#     avg_age_female = df[df['Sex'] == 'female']['Age'].mean()
#     result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
#     return json.dumps(result_dict)
#
#
# print(foo(reviews))
# print(avg_age_by_gender(reviews))

################################


# Задача 2. Фильтрация пассажиров по возрасту и полу

# Написать функцию, которая должна отфильтровать DataFrame, чтобы в нем остались
# только мужчины старше 50 лет или женщины младше 30 лет. Функция должна вернуть
# отфильтрованный DataFrame в формате JSON.

# def foo(df):
#
#     age = df[((df['Sex'] == 'male') & (df['Age'] > 50) | (df['Sex'] == 'female') & (df['Age'] < 30))]
#     return age.to_json(orient='records')


############################################################################


# Задача 3. Расчет средней стоимости билета на пассажира по классу

# Написать функцию, которая вычислит среднюю стоимость билета на пассажира для каждого класса.
# Функция принимает датафрейм и должна вернуть результат в виде словаря в формате JSON.

def foo(df):
    group_pclass = df.groupby('Pclass').agg({'Fare': 'mean'})

    df_dict = group_pclass.to_dict()
    data = df_dict['Fare']

    return json.dumps(data)


############################################



print(foo(reviews))










