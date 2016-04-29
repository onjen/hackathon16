import csv
import matplotlib.pyplot as plt
import sys
import numpy as np

def findall(L, value, start=0):
    # generator version
    i = start - 1
    try:
        i = L.index(value, i+1)
        yield i
    except ValueError:
        pass

def readData():
    outdoor_acc = []
    kwh_acc = []
    steps_per_day = 2*60*24
    for i in xrange(1, 6): 
        with open('Anlage' + str(i) + '.csv', 'rb') as csvfile:
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
                    kwh_acc.append(kwh/60/24)
                    count = 1
                    outdoor = float(0)
                    kwh = float(0)

    min_temp = sys.maxint
    max_temp = -sys.maxint-1

    rounded_outdoor_acc = []
    for temp in outdoor_acc:
        rounded_outdoor_acc.append(int(temp * 10))

    for temp in rounded_outdoor_acc:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp

    print "Temp range is from " + str(float(min_temp)/10) + " until " + str(float(max_temp)/10)

    energy_per_temp = []
    current_temp = min_temp
    while current_temp <= max_temp:
        count = rounded_outdoor_acc.count(current_temp)
        kwh = float(0)
        for idx in findall(rounded_outdoor_acc, current_temp):
            kwh += kwh_acc[idx]
        if count is not 0:
            energy_per_temp.append([float(current_temp)/10, kwh/count])
        current_temp += 1

    print energy_per_temp

    temps = []
    kwh = []
    for item in energy_per_temp:
        temps.append(item[0])
        kwh.append(item[1])

    return {'temps':temps,'kwh':kwh}

def getRegressionFor(x, y, xp):
    z = np.polyfit(x, y, 1)

    print z
    
    p = np.poly1d(z)
    return p(xp)

def main():
    data = readData();
    x = np.array(data['temps'])
    y = np.array(data['kwh'])

    xp = np.linspace(-7, 12, 100)
    _ = plt.plot(x, y, '-', xp, getRegressionFor(x,y,xp), '-')
    plt.ylim(0,0.2)
    plt.show()


if __name__ == "__main__":
        main()
