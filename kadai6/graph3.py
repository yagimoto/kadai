import openpyxl
import matplotlib.pyplot as plt
import openpyxl.utils
import openpyxl.utils.datetime

wb = openpyxl.load_workbook('陽性者数.xlsx')

sheet = wb['yousei2021']

area = {"data": "A184:A214", "count": "B184:B214"}

sum_count = []
sum = 0
for cell in sheet[area["count"]]:
    value = cell[0].value
    sum = sum + value
    sum_count.append(sum)

count = []
for cell in sheet[area["count"]]:
    value = cell[0].value
    count.append(value)

data = []
for cell in sheet[area["data"]]:
    value = cell[0].value
    value = openpyxl.utils.datetime.from_excel(value)
    data.append(value)


plt.plot(data, count)
plt.plot(data, sum_count)
plt.savefig("3.svg")
plt.show()
