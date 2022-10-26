import csv
import re

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
# from sklearn import datasets

# data = pd.read_csv('hockey_players.csv', delimiter=',',encoding='utf-8')

#
with open('hockey_players.csv', 'r',encoding='utf-8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row)
#Круговая диаграмма
# dict = {'Goalkeeper':'','Defender':'','Forward':''}
# sum_Goalkeeper = 0
# sum_Defender = 0
# sum_Forward = 0
# with open('hockey_players.csv', 'r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#         if row[4] == "G":
#             sum_Goalkeeper += 1
#             dict['Goalkeeper'] = sum_Goalkeeper
#         if row[4] == "D":
#             sum_Defender += 1
#             dict['Defender'] = sum_Defender
#         if row[4] == "F":
#             sum_Forward += 1
#             dict['Forward'] = sum_Forward
# labels = []
# sizes = []
# for x, y in dict.items():
#     labels.append(x)
#     sizes.append(y)
# plt.pie(sizes, labels=labels, autopct='%.2f%%')
# plt.title('Распределение позиций между хоккеистами', fontsize=10)
# plt.show()
# Столбчатая диаграмма
# dict = {"Январь": 0,"Февраль": 0,"Март": 0,"Апрель": 0,"Май": 0,"Июнь": 0,"Июль": 0,"Август": 0,"Сентябрь": 0,"Октябрь": 0,"Ноябрь": 0,"Декабрь": 0,}
# with open('hockey_players.csv', 'r',encoding='utf-8') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         try:
#             x = re.findall("\d+", row[8])
#             if x[1] == "01":
#                 dict['Январь'] += 1
#             if x[1] == "02":
#                 dict['Февраль'] += 1
#             if x[1] == "03":
#                 dict['Март'] += 1
#             if x[1] == "04":
#                 dict['Апрель'] += 1
#             if x[1] == "05":
#                 dict['Май'] += 1
#             if x[1] == "06":
#                 dict['Июнь'] += 1
#             if x[1] == "07":
#                 dict['Июль'] += 1
#             if x[1] == "08":
#                 dict['Август'] += 1
#             if x[1] == "09":
#                 dict['Сентябрь'] += 1
#             if x[1] == "10":
#                 dict['Октябрь'] += 1
#             if x[1] == "11":
#                 dict['Ноябрь'] += 1
#             if x[1] == "12":
#                 dict['Декабрь'] += 1
#         except:
#             continue
# month = []
# col = []
# for x, y in dict.items():
#     month.append(x)
#     col.append(y)
# plt.bar(month, col)
# plt.title('Распределение хоккеистов по месяцам рождения')
# plt.xlabel('Месяц')
# plt.ylabel('Человек')
# plt.show()
# Гистограмма
# with open('hockey_players.csv', 'r',encoding='utf-8') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     year = []
#     for row in plots:
#         year.append(row[0])
#     year = set(year)
#     year.remove('year')
#     year_list = []
#     for i in range(1,len(year)):
#         year_list.append(i)
#
#     years_dict = dict.fromkeys(year,0)
#
# print(years_dict)
# sum = 0

# with open('hockey_players.csv', 'r', encoding='utf-8') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         sum +=1
#         for el in year:
#             if row[0] == el:
#                 years_dict[el] += 1
#     sum = sum - 1
# for x,y in years_dict.items():
#     x = years_dict.get(x)
#     result = int(sum) / int(x)
#     years_dict[x] = float(result)
#     print(result)
# print(sum)
# посчитать количесвтво игроков каждого года и общее количество игроков и поделить на количество
# plt.title('Распределение хоккеистов по количеству участий в ЧМ')
# plt.hist(year_list,edgecolor='black', bins =50)
# plt.title('Распределение хоккеистов по количеству участий в ЧМ')
# plt.xlabel('Количество ЧМ')
# plt.ylabel('Доля')
# plt.show()
#График
with open('hockey_players.csv', 'r', encoding='utf-8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    years = []
    dict = {'Goalkeeper':'','Defender':'','Forward':''}
    height_Goalkeeper = []
    height_Defender = []
    height_Forward = []
    for row in plots:
        if row[0] and row[0] != 'year' not in years:
            years.append(int(row[0]))
        if row[4] == "G":
            height_Goalkeeper.append(row[6])
            dict['Goalkeeper'] = height_Goalkeeper
        if row[4] == "D":
            height_Defender.append(row[6])
            dict['Defender'] = height_Defender
        if row[4] == "F":
            height_Forward.append(row[6])
            dict['Forward'] = height_Forward
    years =sorted(set(years))
    years_dict = {}
    for god in years:
        years_dict[god] = []
    with open('hockey_players.csv', 'r', encoding='utf-8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        x = []
        y = []
        for row in plots:
            x.append(row[0])
            y.append(row[6])
            for key,el in years_dict.items():
                if row[0] == str(key):
                    years_dict[key].append(int(row[6]))
print(years_dict)


# average = {key: round(sum(value)/len(value)) for key, value in years_dict.items()}
#
# print(average)
# print(dict)
# god = []
# height = []
# for x, y in average.items():
#     god.append(x)
#     height.append(y)
# x = god
# y = height
plt.title('Тренды изменения роста игрока для каждой позиции')
plt.xlabel('Год ЧМ')
plt.ylabel('Рост(см.)')
plt.plot(x,y)
plt.legend(loc=4)
plt.show()
fig = plt.figure()
#
# ax_1 = fig.add_subplot(2, 2, 1)
# ax_2 = fig.add_subplot(2, 2, 2)
# ax_3 = fig.add_subplot(2, 2, 3)
# ax_4 = fig.add_subplot(2, 2, 4)
# fig.suptitle(f'Хоккейная статистика ЧM:{years}')
# ax_1.set(title = 'ax_1', xticks=[], yticks=[])
# ax_2.set(title = 'Тренды изменения роста игрока для каждой позиции', xticks=[], yticks=years)
# ax_3.set(title = 'Распределение хоккеистов по месяцам рождения', xticks=[], yticks=[])
# ax_4.set(title = 'Распределение позиций между хоккеистами', xticks=[], yticks=[])
#
# plt.show()