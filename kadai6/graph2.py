import openpyxl
import matplotlib.pyplot as plt
import openpyxl.utils
import openpyxl.utils.datetime

wb = openpyxl.load_workbook('陽性者数.xlsx')

sheet = wb['yousei2021']

count = []
sum = 0
for cell in sheet['B1:B222']:
    value = cell[0].value
    sum = sum + value
    count.append(sum)

data = []
for cell in sheet['A1:A222']:
    value = cell[0].value
    value = openpyxl.utils.datetime.from_excel(value)
    data.append(value)

plt.plot(data, count)
plt.savefig("2.svg")
plt.show()
