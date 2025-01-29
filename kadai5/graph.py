import csv
import pprint
import matplotlib.pyplot as plt

with open('data.csv') as f:
    reader = csv.reader(f)

    l = [row for row in reader]

months = list()
for i in range(1,13):
    months.append(i)

for j in range(5):
    temp = []
    for i in range(12):
        temp.append(float(l[i + 5 + j * 12][1]))
        plt.plot(temp)

plt.title("Okinawa's average monthly temperatures")
plt.xlabel("month")
plt.ylabel("temp")
plt.legend(["2020","2021", "2022", "2023", "2024"])
plt.axis(xmin=-0.5,xmax=11.5,ymin=0,ymax=35)
plt.grid()

plt.savefig("graph.svg")
