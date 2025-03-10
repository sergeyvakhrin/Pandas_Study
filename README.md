https://skypro.yonote.ru/share/bbb687d2-98be-4add-a896-d61e4cdbdd03/doc/biblioteka-pandas-csv-5aY6yjDenj


Библиотека pandas, csv
📝


 Цели урока
Понять, как работать с библиотекой Pandas для анализа данных

Освоить основные методы работы с DataFrame

Изучить группировку, сортировку и фильтрацию данных

Научиться агрегировать данные по нескольким столбцам

 



Введение в урок
 

В этом уроке мы будем изучать библиотеку pandas - мощный инструмент для анализа данных в Python. pandas предоставляет высокоуровневый интерфейс для обработки и анализа данных, включая методы для чтения и записи данных из различных источников, работы с пропущенными значениями и многим другим.

 

На протяжении урока мы будем использовать DataFrame - основной объект pandas для работы с данными. Мы изучим, как создавать, индексировать и изменять DataFrame, а также как осуществлять основные операции с ним, такие как фильтрация, группировка и сортировка данных.

 

Мы также рассмотрим, как агрегировать данные по нескольким столбцам, чтобы получить общую информацию о наборе данных. В конце урока вы научитесь применять полученные знания для анализа и обработки реальных наборов данных.

 



Библиотека csv
 



Play Video
 

Библиотека csv в Python предоставляет возможность работать с CSV-файлами. CSV (Comma-Separated Values) - это формат хранения данных, в котором значения разделены запятыми.

 

Формат CSV-файла

 

CSV-файл представляет собой текстовый файл, в котором каждая строка соответствует строке таблицы, а каждое значение в строке разделено запятой или другим символом. Например, CSV-файл, содержащий таблицу со списком имен, возрастов и пола, может выглядеть следующим образом:

 

Name,Age,Gender
Alice,25,Female
Bob,30,Male
Charlie,35,Male

 

Чтение CSV-файла

 

Для чтения CSV-файла в Python нужно использовать модуль csv. Для начала нужно импортировать модуль:

 

import csv

 

Затем можно открыть CSV-файл и прочитать его содержимое:

 

with open('file.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

 

Этот код открывает файл file.csv и читает его содержимое, выводя каждую строку в консоль. Функция csv.reader принимает в качестве аргумента открытый файл и возвращает итератор, который можно использовать для чтения строк файла.

 

Если CSV-файл использует другой символ в качестве разделителя, это можно указать в качестве аргумента функции csv.reader. Например, для CSV-файла, в котором значения разделены точкой с запятой, можно использовать следующий код:

 

with open('file.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

 

Запись CSV-файла

 

Для записи CSV-файла в Python также нужно использовать модуль csv. Например, можно создать список строк и записать его в CSV-файл:

 

import csv

rows = [
    ['Name', 'Age', 'Gender'],
    ['Alice', '25', 'Female'],
    ['Bob', '30', 'Male'],
    ['Charlie', '35', 'Male'],
]

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

 

Этот код создает список строк rows и записывает его в файл file.csv. Функция csv.writer принимает в качестве аргумента открытый файл и возвращает объект, который можно использовать для записи строк в файл.

 

Если нужно использовать другой символ в качестве разделителя, это можно указать в качестве аргумента функции csv.writer. Например, для записи CSV-файла со значениями, разделенными точкой с запятой, можно использовать следующий код:

 

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(rows)

 

Использование DictReader и DictWriter

 

Модуль csv также предоставляет DictReader и DictWriter, которые позволяют работать с CSV-файлами как со словарями. Для этого вместо функции csv.reader и csv.writer используются функции csv.DictReader и csv.DictWriter.

 

DictReader позволяет читать CSV-файл и создавать словари из строк файла. Ключами в словаре будут названия столбцов, а значениями - значения в соответствующих ячейках:

 

import csv

with open('file.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'], row['Gender'])

 

DictWriter позволяет записывать словари в CSV-файл. Для этого нужно указать названия столбцов (ключи в словаре) при создании объекта DictWriter, а затем вызывать метод writeheader() для записи заголовка и метод writerow() для записи строк:

 

import csv

rows = [
    {'Name': 'Alice', 'Age': '25', 'Gender': 'Female'},
    {'Name': 'Bob', 'Age': '30', 'Gender': 'Male'},
    {'Name': 'Charlie', 'Age': '35', 'Gender': 'Male'},
]

with open('file.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'Gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

 

Если необходимо использовать другой символ в качестве разделителя, это можно указать в качестве аргумента функций csv.DictReader и csv.DictWriter.

 



Создание и чтение данных в pandas
 



Play Video
 

pandas - это библиотека Python, которая предоставляет возможности для обработки и анализа данных. Она используется для работы с табличными данными, такими как данные из таблиц Excel, CSV или SQL.

 

Для установки библиотеки pandas можно использовать менеджер пакетов pip или poetry:

 

poetry add pandas
# или
pip isntall pandas

 

Чтобы использовать библиотеку pandas в своем коде, ее нужно импортировать. Обычно ее импортируют с сокращенным именем pd:

 

import pandas as pd

 

В pandas есть два основных объекта: DataFrame и Series.

 



DataFrame
 

DataFrame - это таблица. Он содержит массив отдельных записей, каждая из которых имеет определенное значение. Каждая запись соответствует строке (или записи) и столбцу.

 

Например, рассмотрим следующий простой DataFrame:

 

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

 

Результат в консоли:

 



Yes

No

0

50

131

1

21

2

 

В этом примере "0, No" имеет значение 131. Значение "0, Yes" равно 50 и так далее.

 

Записи DataFrame не ограничены целыми числами. Например, вот DataFrame, значения которого являются строками:

 

pd.DataFrame({
    'Bob': ['Мне это понравилось.', 'Это было ужасно.'],
    'Sue': ['Довольно хорошо.', 'Без вкуса.'],
})

 



Bob

Sue

0

Мне это понравилось.

Довольно хорошо.

1

Это было ужасно.

Без вкуса.

 

Мы используем конструктор pd.DataFrame() для создания этих объектов DataFrame. Синтаксис для объявления нового объекта DataFrame заключается в словаре, ключи которого являются именами столбцов (Bob и Sue в этом примере), а значения - список записей. Это один из стандартных способов создания нового объекта DataFrame.

 

По умолчанию каждой строке в таблице DataFrame присваивается метка, значение которой возрастает от 0 (0, 1, 2, 3, ...). Иногда это нормально, но бывает мы захотим сами присвоить эти метки.

 

Список меток строк, используемых в DataFrame, известен как Index. Мы можем назначить ему значения, используя параметр index в нашем конструкторе:

 

pd.DataFrame(
    {
        "Bob": ["Мне это понравилось.", "Это было ужасно."],
        "Sue": ["Довольно хорошо.", "Без вкуса."],
    },
    index=["Товар A", "Товар B"],
)

 



Bob

Sue

Товар A

Мне это понравилось.

Довольно хорошо.

Товар B

Это было ужасно.

Без вкуса.

 



Series
 

Series является последовательностью значений данных. Если DataFrame - это таблица, то Series - это список. Series  можно создать используя список:

 

pd.Series([1, 2, 3, 4, 5])
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

 

Series - это, по сути, один столбец DataFrame. Таким образом, вы можете назначить метки строк для Series так же, как и раньше, используя параметр index. Однако у Series нет имени столбца, у него только одно общее имя:

 

pd.Series([30, 35, 40],
          index=['Продажи 2015 года', 'Продажи 2016 года', 'Продажи 2017 года'],
          name='Товар A',
          )
# Продажи 2015 года    30
# Продажи 2016 года    35
# Продажи 2017 года    40
# Name: Товар A, dtype: int64

 

Series и DataFrame тесно связаны между собой. Полезно думать о DataFrame как о просто наборе Series, "склеенных вместе".

 



Чтение файлов данных
 

Умение создавать DataFrame или Series вручную очень полезно. Но, в большинстве случаев, мы не будем создавать свои данные вручную. Вместо этого мы будем работать с данными, которые уже существуют.

 

Данные могут храниться в любой из множества различных форм и форматов. Намного наиболее базовым из них является скромный файл CSV. Когда вы открываете файл CSV, вы получаете что-то вроде этого:

 

Товар A,Товар B,Товар C,
30,21,9,
35,34,1,
41,11,11

 

Таким образом, файл CSV представляет собой таблицу значений, разделенных запятыми.

 

Теперь посмотрим, как выглядит реальный набор данных, когда мы считываем его в DataFrame. Мы используем функцию pd.read_csv() для чтения данных в DataFrame. Это выглядит следующим образом:

 

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

 

 Скачайте и распакуйте zip-архив и используйте полученный csv-файл.

zip
winemag-data-130k-v2.csv.zip

17.18 MB
Для чтения файлов Excel (.xls или .xlsx) можно использовать метод pd.read_excel(). Он работает аналогично pd.read_csv(), но имеет несколько дополнительных параметров, таких как название листа или столбца, который следует использовать в качестве индекса.



 

Мы можем использовать атрибут shape, чтобы проверить, каков размер результирующего DataFrame:

 

wine_reviews.shape
# (129971, 14)

 

Таким образом, наш новый DataFrame содержит 130 000 записей, разбитых на 14 разных столбцов. Это почти 2 миллиона записей!

 

Мы можем изучить содержимое полученного DataFrame, используя команду head(), которая получает первые пять строк:

 

wine_reviews.head()

 



Unnamed: 0

country

description

designation

points

price

province

region_1

region_2

taster_name

taster_twitter_handle

title

variety

winery

0

0

Italy

Aromas include tropical fruit, broom, brimston...

Vulkà Bianco

87

NaN

Sicily & Sardinia

Etna

NaN

Kerin O’Keefe

@kerinokeefe

Nicosia 2013 Vulkà Bianco (Etna)

White Blend

Nicosia

1

1

Portugal

This is ripe and fruity, a wine that is smooth...

Avidagos

87

15.0

Douro

NaN

NaN

Roger Voss

@vossroger

Quinta dos Avidagos 2011 Avidagos Red (Douro)

Portuguese Red

Quinta dos Avidagos

2

2

US

Tart and snappy, the flavors of lime flesh and...

NaN

87

14.0

Oregon

Willamette Valley

Willamette Valley

Paul Gregutt

@paulgwine

Rainstorm 2013 Pinot Gris (Willamette Valley)

Pinot Gris

Rainstorm

3

3

US

Pineapple rind, lemon pith and orange blossom ...

Reserve Late Harvest

87

13.0

Michigan

Lake Michigan Shore

NaN

Alexander Peartree

NaN

St. Julian 2013 Reserve Late Harvest Riesling ...

Riesling

St. Julian

4

4

US

Much like the regular bottling from 2012, this...

Vintner's Reserve Wild Child Block

87

65.0

Oregon

Willamette Valley

Willamette Valley

Paul Gregutt

@paulgwine

Sweet Cheeks 2012 Vintner's Reserve Wild Child...

Pinot Noir

Sweet Cheeks

 

Функция pd.read_csv() хорошо оснащена, с более чем 30 необязательными параметрами, которые вы можете указать. Например, вы можете увидеть в этом наборе данных, что файл CSV имеет встроенный индекс, который pandas не смог автоматически определить. Чтобы заставить pandas использовать этот столбец для индекса (вместо создания нового с нуля), мы можем указать index_col.

 

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0) 
wine_reviews.head()

 



country

description

designation

points

price

province

region_1

region_2

taster_name

taster_twitter_handle

title

variety

winery

0

Italy

Aromas include tropical fruit, broom, brimston...

Vulkà Bianco

87

NaN

Sicily & Sardinia

Etna

NaN

Kerin O’Keefe

@kerinokeefe

Nicosia 2013 Vulkà Bianco (Etna)

White Blend

Nicosia

1

Portugal

This is ripe and fruity, a wine that is smooth...

Avidagos

87

15.0

Douro

NaN

NaN

Roger Voss

@vossroger

Quinta dos Avidagos 2011 Avidagos Red (Douro)

Portuguese Red

Quinta dos Avidagos

2

US

Tart and snappy, the flavors of lime flesh and...

NaN

87

14.0

Oregon

Willamette Valley

Willamette Valley

Paul Gregutt

@paulgwine

Rainstorm 2013 Pinot Gris (Willamette Valley)

Pinot Gris

Rainstorm

3

US

Pineapple rind, lemon pith and orange blossom ...

Reserve Late Harvest

87

13.0

Michigan

Lake Michigan Shore

NaN

Alexander Peartree

NaN

St. Julian 2013 Reserve Late Harvest Riesling ...

Riesling

St. Julian

4

US

Much like the regular bottling from 2012, this...

Vintner's Reserve Wild Child Block

87

65.0

Oregon

Willamette Valley

Willamette Valley

Paul Gregutt

@paulgwine

Sweet Cheeks 2012 Vintner's Reserve Wild Child...

Pinot Noir

Sweet Cheeks

 



Индексирование, выбор и присваивание
 



Play Video
 

import pandas as pd
reviews =pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

 

Датасет, с которым работаем в коде, содержит данные о рейтингах и описаниях вин из различных регионов мира.

 



Доступ к столбцам таблицы
 

Чтобы получить доступ к столбцу 'country' в датафрейме reviews, можно использовать обращение через точку (reviews.country) или через квадратные скобки и имя столбца в виде строки (reviews['country']). Например:

 

# Использование обращения через точку
reviews.country

# Использование обращения через квадратные скобки и имя столбца в виде строки
reviews['country']


 

Оба варианта эквивалентны и возвращают Series, содержащий значения из столбца country.

 

Чтобы получить конкретное значение из столбца country, можно использовать обращение по индексу, как в случае с обычным списком. Например:

 

# Обращение к первому значению в столбце 'country' через обращение через квадратные скобки
reviews['country'][0]

# Обращение к первому значению в столбце 'country' через обращение через точку
reviews.country[0]


 

Оба варианта эквивалентны и возвращают строковое значение из первой строки в столбце country.

 



Индексация в pandas
 

Индексация с помощью iloc

 

pandas использует iloc для индексации по числовому значению, то есть по порядковому номеру строки или столбца. Индексация iloc работает следующим образом:

 

reviews.iloc[0] - возвращает первую строку в датафрейме reviews.

reviews.iloc[:, 0] - возвращает первый столбец в датафрейме reviews.

reviews.iloc[:3, 0] - возвращает первые три строки в первом столбце датафрейма reviews.

reviews.iloc[1:3, 0] - возвращает вторую и третью строки в первом столбце датафрейма reviews.

reviews.iloc[[0, 1, 2], 0] - возвращает первые три строки в первом столбце датафрейма reviews.

reviews.iloc[-5:] - возвращает последние пять строк в датафрейме reviews.

 

Обратите внимание, что индексация ilocвозвращает новый датафрейм, состоящий из выбранных строк и столбцов. Если вы хотите изменить исходный датафрейм, используйте индексацию по меткам (loc).

 

Индексация с помощью loc

 

pandas использует loc для индексации по меткам, то есть по именам строк и столбцов. Индексация loc работает следующим образом:

 

reviews.loc[0, 'country'] - возвращает значение в первой строке и столбце country в датафрейме reviews.

reviews.loc[:, 'country'] - возвращает все значения в столбце country в датафрейме reviews.

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']] - возвращает все значения в столбцах taster_name, taster_twitter_handle, и points в датафрейме reviews.

 

Обратите внимание, что индексация loc также возвращает новый датафрейм, состоящий из выбранных строк и столбцов. Если вы хотите изменить исходный датафрейм, используйте индексацию по меткам (loc).

 



Управление индексом
 

Метод set_index() является одним из способов управления индексом в pandas. Он позволяет установить один или несколько столбцов в качестве индекса датафрейма.

 

Например, если мы хотим установить столбец 'title' в качестве индекса для датафрейма reviews, мы можем использовать следующий код:

 

reviews.set_index('title')

 

Этот код создаст новый датафрейм, в котором индексом будет столбец 'title'. Обратите внимание, что этот метод не изменяет исходный датафрейм, он создает новый датафрейм с новым индексом.

 

Вы также можете установить несколько столбцов в качестве индекса, передав список имен столбцов в метод set_index(). Например:

 

reviews.set_index(['title', 'country'])

 

Этот код создаст новый датафрейм, в котором индексом будет комбинация столбцов 'title' и 'country'.

 

Использование метода set_index() особенно полезно, когда вы хотите работать с данными, где определенный столбец является уникальным идентификатором каждой строки в датафрейме. В этом случае установка этого столбца в качестве индекса может существенно ускорить доступ к данным в датафрейме.

 



Отбор по условию
 

pandas позволяет выбирать строки или столбцы, основываясь на заданных условиях.

 

Например, чтобы выбрать все строки, где значение в столбце country равно 'Italy', мы можем использовать следующий код:

 

reviews.loc[reviews.country == 'Italy']

 

Этот код использует функцию loc для выбора строк, где значение в столбце country равно 'Italy'.

 

Мы также можем комбинировать несколько условий с помощью логических операторов. Например, чтобы выбрать все строки, где значение в столбце country равно 'Italy' и значение в столбце points больше или равно 90, мы можем использовать следующий код:

 

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

 

Здесь мы используем оператор & для объединения двух условий.

 

Мы также можем использовать оператор | для выбора строк, которые соответствуют любому из условий. Например, чтобы выбрать все строки, где значение в столбце country равно либо 'Italy', либо значение в столбце points больше или равно 90, мы можем использовать следующий код:

 

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

 

Мы также можем использовать функцию isin для выбора строк, где значение в столбце country равно либо 'Italy', либо 'France'. Например:

 

reviews.loc[reviews.country.isin(['Italy', 'France'])]

 

Наконец, мы можем использовать функцию notnull для выбора строк, где значение в столбце price не равно NaN. Например:

 

reviews.loc[reviews.price.notnull()]

 

Это лишь несколько примеров того, как можно выполнить условный отбор в pandas.

 



Присваивание данных
 

Чтобы присвоить данные датафрейму pandas, можно использовать обращение через квадратные скобки и имя столбца в виде строки. Например, чтобы присвоить значение 'everyone' всем значениям в столбце critic в датафрейме reviews, мы можем использовать следующий код:

 

reviews['critic'] = 'everyone'

 

Этот код присваивает значение 'everyone' всем значениям в столбце critic в датафрейме reviews.

 

Чтобы добавить новый столбец в датафрейм pandas, можно использовать обращение через квадратные скобки и имя нового столбца в виде строки. Например, чтобы добавить столбец index_backwards, который содержит индексы датафрейма reviews в обратном порядке, мы можем использовать следующий код:

 

reviews['index_backwards'] = range(len(reviews), 0, -1)


 

Этот код создает новый столбец index_backwards в датафрейме reviews и присваивает ему значения, равные индексам датафрейма в обратном порядке.

 



Статистика по данным и отображения
 

Play Video


Методы для знакомства с данными
 

Следующие методы позволяют получить быстрый обзор данных в таблице. Рассмотрим несколько примеров:

 

reviews.points.describe() выведет основные статистические характеристики столбца points, такие как среднее, стандартное отклонение, максимальное и минимальное значение, медиану и квартили.

count    129971.000000
mean         88.447138
             ...
75%          91.000000
max         100.000000
Name: points, Length: 8, dtype: float64

reviews.taster_name.describe() выведет статистические характеристики столбца taster_name, такие как количество уникальных значений, наиболее часто встречающееся имя дегустатора (top), количество упоминаний этого имени (freq).

reviews.points.mean() выведет среднее значение столбца points.

reviews.taster_name.unique() выведет список уникальных имен дегустаторов.

reviews.taster_name.value_counts() выведет количество упоминаний каждого имени дегустатора.

Roger Voss           25514
Michael Schachner    15134
                     ...
Fiona Adams             27
Christina Pickard        6
Name: taster_name, Length: 19, dtype: int64

 



map
 

В Python есть функция map, которая позволяет применять функцию к каждому элементу списка. В науке о данных мы часто хотим преобразовывать данные из одного формата в другой. Предположим, что мы хотим перевести оценки вина из 100-балльной шкалы в 0-балльную. Мы можем сделать это с помощью map.

 

review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

 

Или мы можем использовать map для измерения длины описания вина в датасете. Для этого мы можем создать новый столбец description_length, который содержит длину каждого описания вина в символах.

 

reviews['description_length'] = reviews.description.map(len)

 

Теперь мы можем использовать новый столбец для анализа длины описаний:

 

reviews['description_length'].describe()

 

Также мы можем применить функцию к каждой строке в DataFrame, используя apply.

 

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

 

Простейший пример на axis

Рассмотрим DataFrame, состоящий из двух столбцов:

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

Если мы применим функцию sum к DataFrame с параметром axis=0, то она просуммирует значения столбцов:

df.sum(axis=0)

A    6
B    15
dtype: int64

Если же мы применим функцию с параметром axis=1, то она просуммирует значения строк:

df.sum(axis=1)

0     5
1     7
2    9
dtype: int64

То есть, параметр axis позволяет задать направление, по которому нужно применять функцию к DataFrame.

 

Вместо использования apply мы также можем использовать простое математическое выражение.

 

review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

 

Или объединить столбцы, используя оператор +.

 

reviews.country + " - " + reviews.region_1

 



Группировка и сортировка
 



Play Video
 



Группировка данных
 

Часто при работе с данными возникает необходимость группировать их по определенным критериям. Например, мы можем хотеть узнать среднюю цену вина для каждой страны. Для этого мы можем использовать функцию groupby:

 

country_grouped = df.groupby('country')
mean_price_by_country = country_grouped['price'].mean()
print(mean_price_by_country)

 

Мы используем функцию groupby для группировки данных по столбцу 'country'. Затем мы используем столбец 'price' и функцию mean, чтобы вычислить среднюю цену для каждой группы. Результатом является новая таблица, в которой строки представляют отдельные страны, а столбцы - среднюю цену.

 



Сортировка данных
 

Чтобы отсортировать данные в таблице, мы можем использовать функцию sort_values. Например, мы можем отсортировать данные по цене в порядке убывания:

 

sorted_by_price = df.sort_values('price', ascending=False)
print(sorted_by_price.head())

 

Мы используем функцию sort_values для сортировки данных по столбцу 'price'. Параметр ascending=False указывает, что мы хотим сортировать данные в порядке убывания. Результатом является новая таблица, в которой строки отсортированы в порядке убывания цены.

 



Группировка и сортировка данных
 

Мы также можем использовать функцию groupby и sort_values вместе. Например, мы можем отсортировать вина по цене в каждой стране:

 

country_grouped = df.groupby('country')
sorted_by_price_and_country = country_grouped.apply(lambda x: x.sort_values('price', ascending=False))
print(sorted_by_price_and_country.head())

 

Мы сначала используем функцию groupby для группировки данных по странам. Затем мы применяем функцию sort_values к каждой группе с помощью функции apply. Результатом является новая таблица, в которой вина отсортированы по цене в каждой стране.

 



Фильтрация данных
 

Pandas также предоставляет удобный способ фильтровать данные. Например, мы можем выбрать все вина, которые стоят больше 100 долларов:

 

expensive_wines = df[df['price'] > 100]
print(expensive_wines.head())

 

Мы используем оператор > для сравнения значения в столбце 'price' с числом 100. Результатом является новая таблица, в которой только те строки, где стоимость вина больше 100 долларов.

 



Группировка и фильтрация данных
 

Мы можем использовать функцию groupby в сочетании с фильтрацией данных. Например, мы можем выбрать только те вина из Италии, которые стоят больше 100 долларов:

 

italian_wines = df[df['country'] == 'Italy']
expensive_italian_wines = italian_wines[italian_wines['price'] > 100]
print(expensive_italian_wines.head())

 

Мы сначала выбираем все вина из Италии, используя оператор ==. Затем мы выбираем только те строки, где стоимость вина больше 100 долларов. Результатом является новая таблица, в которой только те вина из Италии, которые стоят больше 100 долларов.

 



Группировка и агрегация данных
 

Мы можем использовать функцию groupby для агрегации данных по нескольким столбцам. Например, мы можем вычислить среднюю цену и рейтинг для каждой страны:

 

country_grouped = df.groupby('country')
mean_price_and_rating_by_country = country_grouped.agg({'price': 'mean', 'points': 'mean'})
print(mean_price_and_rating_by_country.head())

 

Мы используем функцию agg для агрегации данных по столбцам 'price' и 'points'. Результатом является новая таблица, в которой строки представляют отдельные страны, а столбцы - среднюю цену и рейтинг.

 



Практические задачи
 

В задачах используется датасет "titanic.csv".

 

Датасет "titanic.csv" содержит информацию о пассажирах корабля "Титаник", включая их возраст, пол, класс билета и информацию о том, выжили ли они в крушении корабля. Датасет содержит 891 строку и 12 столбцов:

 

PassengerId - уникальный идентификатор пассажира

Survived - указывает, выжил пассажир или нет (0 - не выжил, 1 - выжил)

Pclass - класс билета (1 - первый класс, 2 - второй класс, 3 - третий класс)

Name - имя пассажира

Sex - пол пассажира

Age - возраст пассажира

SibSp - количество братьев, сестер, супругов на борту

Parch - количество родителей или детей на борту

Ticket - номер билета

Fare - цена билета

Cabin - номер каюты

Embarked - порт посадки (C - Шербур, Q - Квинстаун, S - Саутгемптон)

 



csv
titanic.csv

60.30 kB
 



Задача 1: Расчет среднего возраста пассажиров по полу
 

Написать функцию, которая принимает на вход DataFrame из датасета "Titanic.csv". Функция должна вычислить средний возраст мужчин и женщин отдельно и вернуть результат в виде словаря в формате JSON.

 

Решение

 

import pandas as pd
import json

def avg_age_by_gender(df):
    avg_age_male = df[df['Sex'] == 'male']['Age'].mean()
    avg_age_female = df[df['Sex'] == 'female']['Age'].mean()
    result_dict = {'Мужчины': avg_age_male, 'Женщины': avg_age_female}
    return json.dumps(result_dict)


 

Тест

 

import json
import pytest
import pandas as pd

@pytest.fixture
def titanic_df():
    sample_dict = {'PassengerId': [1, 2, 3, 4, 5],
                   'Survived': [0, 1, 1, 1, 0],
                   'Pclass': [3, 1, 3, 1, 3],
                   'Name': ['name1', 'name2', 'name3', 'name4', 'name5'],
                   'Sex': ['male', 'female', 'female', 'female', 'male'],
                   'Age': [22.0, 38.0, 26.0, 35.0, 35.0],
                   'SibSp': [1, 1, 0, 1, 0],
                   'Parch': [0, 0, 0, 0, 0],
                   'Ticket': ['tic1', 'tic2', 'tic3', 'tic4', 'tic5'],
                   'Fare': [7.3, 71.3, 7.9, 53.1, 8.1],
                   'Cabin': [None, 'C85', None, 'C123', None],
                   'Embarked': ['S', 'C', 'S', 'S', 'S']}
    return pd.DataFrame(sample_dict)

def test_avg_age_by_gender(titanic_df):
    expected_result = {'Мужчины': 28.5, 'Женщины': 29.7}
    assert avg_age_by_gender(titanic_df) == json.dumps(expected_result)

 



Задача 2: Фильтрация пассажиров по возрасту и полу
 

Написать функцию, которая должна отфильтровать DataFrame, чтобы в нем остались только мужчины старше 50 лет или женщины младше 30 лет. Функция должна вернуть отфильтрованный DataFrame в формате JSON.

 

Решение:

 

import pandas as pd
import json

def filter_passengers(df):
    result_df = df[((df['Sex'] == 'male') & (df['Age'] > 50)) | ((df['Sex'] == 'female') & (df['Age'] < 30))]
    return result_df.to_json(orient='records')


 

Тест:

 

import pytest
import pandas as pd

# здесь фикстура из теста предыдущего задания

def test_filter_passengers(titanic_df):
    expected_result = titanic_df.iloc[1:4].to_json(orient='records')
    assert filter_passengers(titanic_df) == expected_result

 



Задача 3: Расчет средней стоимости билета на пассажира по классу
 

Написать функцию, которая вычислит среднюю стоимость билета на пассажира для каждого класса. Функция принимает датафрейм и должна вернуть результат в виде словаря в формате JSON.

 

Решение:

 

import pandas as pd
import json

def fare_per_passenger_by_class(df):
    total_fare_by_class = df.groupby('Pclass')['Fare'].sum()
    total_passengers_by_class = df.groupby('Pclass')['PassengerId'].count()
    avg_fare_per_passenger_by_class = total_fare_by_class / total_passengers_by_class
    result_dict = avg_fare_per_passenger_by_class.to_dict()
    return json.dumps(result_dict)


 

Тест:

 

import json
import pytest
import pandas as pd

# здесь фикстура из теста предыдущего задания

def test_fare_per_passenger_by_class(titanic_df):
    expected_result = {'1': 62.2, '3': 7.3}
    assert fare_per_passenger_by_class(titanic_df) == json.dumps(expected_result)

 



Итоги урока
 

pandas - библиотека на языке Python для работы с данными в таблицах.

DataFrame - таблица с данными в pandas.

С помощью head() можно вывести первые несколько строк таблицы.

С помощью shape можно узнать размер таблицы.

С помощью describe() можно получить основную статистическую информацию по таблице.

С помощью value_counts() можно получить количество уникальных значений в столбце.

С помощью map() можно применять функцию к каждому элементу списка.

С помощью groupby() можно группировать данные по определенным критериям.

С помощью sort_values() можно сортировать данные в таблице.

С помощью фильтрации данных можно выбрать только те строки, которые удовлетворяют определенным условиям.

С помощью agg() можно агрегировать данные по нескольким столбцам.

 



Быстрые команды в pandas & csv
 

Ключевая тема

Пояснение

Чтение данных

pd.read_csv('file.csv')
Просмотр данных

df.head()
Выбор столбца

df['column_name']
Выбор нескольких столбцов

df[['column_name_1', 'column_name_2']]
Фильтрация данных

df[df['column_name'] > value]
Группировка данных

df.groupby('column_name').agg({'column_to_agg': 'function'})
Сортировка данных

df.sort_values('column_name', ascending=False)
Создание нового столбца

df['new_column'] = df['column_1'] + df['column_2']
 



Практическая реализация
 

Применить функцию map для перевода оценок вина из 100-балльной шкалы в 0-бальную.

 

df['points'] = df['points'].map(lambda x: x-100)


 

Применить функцию map для измерения длины описания вина в датасете.

 

df['description_length'] = df['description'].map(len)


 

Вычислить среднюю цену вина для каждой страны с помощью метода groupby.

 

country_grouped = df.groupby('country')
mean_price_by_country = country_grouped['price'].mean()
print(mean_price_by_country.head())


 

Отсортировать данные по цене в порядке убывания с помощью метода sort_values.

 

sorted_df = df.sort_values('price', ascending=False)
print(sorted_df.head())


 

Выбрать все вина, которые стоят больше 100 долларов с помощью метода filter.

 

expensive_wines = df.filter(items=['country', 'price', 'points']).loc[df['price'] > 100]
print(expensive_wines.head())


 

Выбрать только те вина из Италии, которые стоят больше 100 долларов, используя методы filter и groupby.

 

italian_wines = df.filter(items=['country', 'price', 'points']).loc[(df['price'] > 100) & (df['country']=='Italy')]
print(italian_wines.head())


 

Вычислить среднюю цену и рейтинг для каждой страны с помощью метода agg.

 

country_grouped = df.groupby('country')
mean_price_and_rating_by_country = country_grouped.agg({'price': 'mean', 'points': 'mean'})
print(mean_price_and_rating_by_country.head())


 



Вопросы для самопроверки
 


Что такое CSV-файлы?


Как прочитать CSV-файл в Pytho


Что такое DictReader и DictWriter?


Что такое DataFrame?


Как создать новый DataFrame?


Что такое Series?


Как прочитать файл CSV в DataFrame?


Что возвращает атрибут shape для DataFrame?


Каким образом работает индексация iloc в pandas?


Для чего используется метод set_index() в pandas?


Как добавить новый столбец в датафрейм pandas?


Какие методы позволяют получить быстрый обзор данных в таблице?


Какие статистические характеристики можно вывести с помощью метода describe()?


Как можно использовать map в pandas?


Какую функцию мы используем для группировки данных??


Какую функцию мы используем для сортировки данных?


Как мы можем фильтровать данные в таблице?
