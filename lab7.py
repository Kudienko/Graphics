import csv
import re
from statistics import mean
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
# Круговая диаграмма
dict = {'Goalkeeper':'','Defender':'','Forward':''}
sum_Goalkeeper = 0
sum_Defender = 0
sum_Forward = 0
with open('hockey_players.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        if row[4] == "G":
            sum_Goalkeeper += 1
            dict['Goalkeeper'] = sum_Goalkeeper
        if row[4] == "D":
            sum_Defender += 1
            dict['Defender'] = sum_Defender
        if row[4] == "F":
            sum_Forward += 1
            dict['Forward'] = sum_Forward
labels = []
sizes = []
for x, y in dict.items():
    labels.append(x)
    sizes.append(y)
plt.pie(sizes, labels=labels, autopct='%.2f%%')
plt.title('Распределение позиций между хоккеистами', fontsize=10)
plt.show()
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
# data = pd.read_csv('hockey_players.csv', encoding="ISO-8859-1", header = 0)
# data1 = data.copy()
# data1.drop_duplicates(subset=['name'], keep='first', inplace=True)
# x1=data['name'].value_counts()
# data['name'].value_counts().hist(grid=False, color='r', figsize=(6,4), edgecolor='black')
# plt.title(u'Распределение хоккеистов по количеству участий в ЧМ')
# plt.xlabel("Количество ЧМ")
# plt.ylabel("Доля")
# plt.show()
#График
# fig, ax2 = plt.subplots(figsize=(10,6))
# ax2.set_title(u'Тренды изменения роста игрока для каждой позиции')
# ax2.set_xlabel("Год ЧМ", fontsize=14)
# ax2.set_ylabel("Рост (см.)", fontsize=14)
# xx = pd.DataFrame()
# data = pd.read_csv('hockey_players.csv', encoding="ISO-8859-1", header = 0)
# data1 = data.copy()
# data1.drop_duplicates(subset=['name'], keep='first', inplace=True)
# x21=data[data['position']=='G'].groupby('year')['height'].mean()
# x22=data[data['position']=='D'].groupby('year')['height'].mean()
# x23=data[data['position']=='F'].groupby('year')['height'].mean()
# xx['height'] = x21.copy()
# xx['year'] = x21.index
# xx2 = pd.DataFrame()
# xx2['height'] = x22.copy()
# xx2['year'] = x22.index
# xx3 = pd.DataFrame()
# xx3['height'] = x23.copy()
# xx3['year'] = x23.index
# z1 = np.polyfit(xx['year'], xx['height'], 1)
# p1 = np.poly1d(z1)
# z2 = np.polyfit(xx2['year'], xx2['height'], 1)
# p2 = np.poly1d(z2)
# z3 = np.polyfit(xx3['year'], xx3['height'], 1)
# p3 = np.poly1d(z3)
# ax2.plot(xx['year'], p1(xx['year']), linestyle='dashed')
# ax2.plot(xx2['year'], p2(xx2['year']), linestyle='dashed')
# ax2.plot(xx3['year'], p3(xx3['year']), linestyle='dashed')
# ax2.legend(['Вратарь', 'Защитник', 'Нападающий'], fontsize=14,loc = 4)
# ax2.tick_params(axis = 'both', labelsize = 14)
# plt.show()
