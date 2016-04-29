import csv
import matplotlib.pyplot as plt
import numpy as np

outdoor_temperatures = []
kwh = []
target = []
days = 1
for i in xrange(1,6):
    anlage = 'Anlage' + str(i) + '.csv'
    with open(anlage, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        max_count = 2*60*24*days
        count = 0
        outdoor_temperature = []
        for row in reader:
            if count > max_count:
                break
            if count is 0:
                count += 1
                continue
            outdoor_temperature.append(row[1])
            target.append(row[2])
            kwh.append(row[3])
            count += 1
    outdoor_temperatures.append(outdoor_temperature)
    print(len(outdoor_temperatures))

plt.plot(outdoor_temperatures[0],'b',outdoor_temperatures[1],'r',
        outdoor_temperatures[2],'g',outdoor_temperatures[3],'y',
        outdoor_temperatures[4],'c')
plt.show()
