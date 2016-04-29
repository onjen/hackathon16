import csv
import matplotlib.pyplot as plt

outdoor_acc = []
kwh_acc = []
steps_per_day = 2*60*24
with open('Anlage5.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    count = 1
    outdoor = float(0)
    kwh = float(0)
    for row in reader:
        if reader.line_num == 1:
            continue
        outdoor += float(row[1])
        kwh += float(row[3])
        count += 1
        if count >= steps_per_day:
            outdoor_acc.append(outdoor/steps_per_day)
            kwh_acc.append(kwh/60/24*-1)
            count = 1
            outdoor = float(0)
            kwh = float(0)

fig, ax1 = plt.subplots()
ax1.plot(outdoor_acc, 'b-')
ax1.set_xlabel('days')
ax1.set_ylabel('avg outdoor temp', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax2 = ax1.twinx()
ax2.plot(kwh_acc,'r-')
ax2.set_ylabel('kwh', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()
