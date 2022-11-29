import csv
import io
import matplotlib.pyplot as plt
from random import randint

visaList = []
mastercardList = []
with io.open('mastercard.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        mastercardList.append(float(row[5]))

with io.open('visa.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        visaList.append(float(row[5]))


def search(list, value):
    for i in range(len(list)):
        if list[i][0] == value:
            return i
    return -1


def probabilty(list):
    list_of_data = []
    for i in range(len(list)):
        index = search(list_of_data, list[i])
        if index > -1:
            list_of_data[index][1] += 1
        else:
            list_of_data.append([list[i], 1])
    for i in range(len(list_of_data)):
        list_of_data[i][1] /= len(list)
    return list_of_data


print('Visa - ', visaList)
print('MasterCard - ', mastercardList)

visaListProbability = probabilty(visaList)
mastercardProbability = probabilty(mastercardList)

print('Visa probabilty - ', visaListProbability)
print('MasterCard probability - ', mastercardProbability)

mastercardMathExpectation = 0
visaMathExcectation = 0
for i in range(len(visaListProbability)):
    visaMathExcectation += visaListProbability[i][0] * visaListProbability[i][1]
    mastercardMathExpectation += mastercardProbability[i][0] * mastercardProbability[i][1]
print("Math expectation visa =", visaMathExcectation)
print("Math expectation masterCard = ", mastercardMathExpectation)

x, y, z = 0, 0, 0
for i in range(len(visaList)):
    x += (visaList[i] - visaMathExcectation) * (mastercardList[i] - mastercardMathExpectation)
    y += (visaList[i] - visaMathExcectation) * (visaList[i] - visaMathExcectation)
    z += (mastercardList[i] - mastercardMathExpectation) * (mastercardList[i] - mastercardMathExpectation)
print('Коэффицент корреляции Пирсона =', x / ((y * z) ** 0.5))

visaList1 = []
mastercardList1 = []

for i in range(len(visaList)):
    visaList1.append(visaList[i])
    mastercardList1.append(mastercardList[i])

for i in range(249):
    index = randint(0, len(visaList1) - 1)
    if visaList1[index]:
        visaList1[index] = []
    if mastercardList1[index]:
        mastercardList1[index] = []

visaList2 = []
visaList3 = []
mastercardList2 = []
mastercardList3 = []
for i in range(len(visaList)):
    visaList2.append(visaList1[i])
    visaList3.append(visaList1[i])
    mastercardList2.append(mastercardList1[i])
    mastercardList3.append(mastercardList1[i])

print('Visa without random data', visaList1)
print('MasterCard without random data', mastercardList1)


def vinzoring(list):
    for i in range(len(list)):
        if not list[i]:
            index = -1
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                index_priveous -= 1
                if index_next < len(list) and list[index_next] != []:
                    index = index_next
                    break
                if index_priveous >= 0 and list[index_priveous] != []:
                    index = index_priveous
                    break
            list[i] = list[index]


vinzoring(visaList1)
vinzoring(mastercardList1)
print('Восстановление с помощью винзорирования')
print('Visa = ', visaList1)
print('MasterCard = ', mastercardList1)


def linear_approximation(list):
    for i in range(len(list)):
        if not list[i]:
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                if index_next >= len(list) or list[index_next] != []:
                    break
            while True:
                index_priveous -= 1
                if index_priveous < 0 or list[index_priveous] != []:
                    break
            if index_next >= len(list):
                index_next = index_priveous - 1
                while True:
                    if index_next >= 0 and list[index_next] != []:
                        break
                    index_next -= 1

            if index_priveous < 0:
                index_priveous = index_next + 1
                while True:
                    if index_priveous < len(list) and list[index_priveous] != []:
                        break
                    index_priveous += 1
            if list[index_priveous] == list[index_next]:
                list[i] = list[index_next]
            else:
                a = (index_priveous - index_next) / (list[index_priveous] - list[index_next])
                b = index_next - a * list[index_next]
                list[i] = (i - b) / a


linear_approximation(visaList2)
linear_approximation(mastercardList2)
print('Восстановление с помощью линейная аппроксимации')
print('Visa = ', visaList2)
print('MasterCard = ', mastercardList2)


def correlation_recovery(list_one, list_two):
    for i in range(len(list_one)):
        if not list_one[i]:
            index = -1
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                index_priveous -= 1
                if index_next < len(list_one) and list_one[index_next] != []:
                    index = index_next
                    break
                if index_priveous >= 0 and list_one[index_priveous] != []:
                    index = index_priveous
                    break
            list_one[i] = (list_two[i] / list_two[index]) * list_one[index]


correlation_recovery(visaList3, mastercardList)
correlation_recovery(mastercardList3, visaList)
print('Востановление с помощью корреляции')
print('Visa = ', visaList3)
print('MasterCard = ', mastercardList3)

fig, ax = plt.subplots(4, 2)
ax[0, 0].set_title("Visa")
ax[0, 0].plot(visaList, color='red')
ax[1, 0].set_title("Винзорирование")  # Visa
ax[1, 0].plot(visaList1, color='green')
ax[1, 0].plot(visaList, color='red')
ax[0, 1].set_title("Обычный набор данных MasterCard")
ax[0, 1].plot(mastercardList, color='black')
ax[1, 1].set_title("Винзорирование")  # MasterCard
ax[1, 1].plot(mastercardList1, color='green')
ax[1, 1].plot(mastercardList, color='black')
ax[2, 0].set_title("Линейная аппроксимация")  # Visa
ax[2, 0].plot(visaList2, color='green')
ax[2, 0].plot(visaList, color='red')
ax[2, 1].set_title("Линейная аппроксимация")  # MasterCard
ax[2, 1].plot(mastercardList2, color='green')
ax[2, 1].plot(mastercardList, color='black')
ax[3, 0].set_title("Корреляционное восстановление")  # Visa
ax[3, 0].plot(visaList3, color='green')
ax[3, 0].plot(visaList, color='red')
ax[3, 1].set_title("Корреляционное восстановление")  # MasterCard
ax[3, 1].plot(mastercardList3, color='green')
ax[3, 1].plot(mastercardList, color='black')
for ax in ax.flat:
    ax.label_outer()
plt.show()
