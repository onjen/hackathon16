import csv
import matplotlib.pyplot as plt

outdoor = []
kwh = []
target = []
days = 1
with open('Anlage3.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    max_count = 2*60*24*days
    count = 0
    for row in reader:
        if count > max_count:
            break
        if count is 0:
            count += 1
            continue
        outdoor.append(row[1])
        target.append(row[2])
        kwh.append(row[3])
        count += 1
        
fig, ax1 = plt.subplots()
ax1.plot(outdoor, 'b-')
ax1.set_xlabel('time in 30s steps')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('outdoor temp', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')
ax2 = ax1.twinx()
ax2.plot(kwh,'r-')
ax2.set_ylabel('kwh', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
ax3 = ax2.twinx()
ax3.plot(target,'g-')
ax3.set_ylabel('target temp', color='g')
for tl in ax3.get_yticklabels():
    tl.set_color('g')
plt.show()
