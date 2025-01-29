import openpyxl
import matplotlib.pyplot as plt
import openpyxl.utils
import openpyxl.utils.datetime

wb = openpyxl.load_workbook('陽性者数.xlsx')

sheet = wb['yousei2021']

count = []
for cell in sheet['B1:B214']:
    value = cell[0].value
    count.append(value)

data = []
for cell in sheet['A1:A214']:
    value = cell[0].value
    value = openpyxl.utils.datetime.from_excel(value)
    data.append(value)

plt.plot(data, count)
plt.savefig("4.svg")
plt.show()
