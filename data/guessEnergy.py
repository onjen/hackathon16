import sqlite3
import sys
import matplotlib.pyplot as plt
import numpy as np
from energyPerTemp import getRegressionFor

def findall(L, value, start=0):
    # generator version
    i = start - 1 
    try:
        i = L.index(value, i+1)
        yield i
    except ValueError:
        pass

def vis(x,y):
    _ = plt.plot(x, y, '-', xp, getRegressionFor(x,y,xp), '-')
    plt.ylim(0,0.05)
    plt.show()

def guess(xp):
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT TARGET, ENERGY FROM DATA")
    targets = []
    energies = []
    for row in cursor:
        targets.append(int(row[0]))
        energies.append(row[1])

    min_target = sys.maxint
    max_target = -sys.maxint-1

    for target in targets:
        if min_target > target:
            min_target = target
        if max_target < target:
            max_target = target

    energyAverages = dict()
    for i in xrange(min_target, max_target):
        count = 0
        energy = float(0)
        index = 0
        for target in targets:
            if target == i:
                count += 1
                energy += energies[index]
            index += 1
        if count is not 0:
            energyAverages[i] = energy/count

    y = np.array(energyAverages.keys())
    x = np.array(energyAverages.values())

#    vis(x,y)
    return getRegressionFor(x,y,xp)

def guess_inverse(xp):
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT TARGET, ENERGY FROM DATA")
    targets = []
    energies = []
    for row in cursor:
        targets.append(int(row[0]))
        energies.append(row[1])

    min_target = sys.maxint
    max_target = -sys.maxint-1

    for target in targets:
        if min_target > target:
            min_target = target
        if max_target < target:
            max_target = target

    energyAverages = dict()
    for i in xrange(min_target, max_target):
        count = 0
        energy = float(0)
        index = 0
        for target in targets:
            if target == i:
                count += 1
                energy += energies[index]
            index += 1
        if count is not 0:
            energyAverages[i] = energy/count

    y = np.array(energyAverages.keys())
    x = np.array(energyAverages.values())

    #vis(x,y)
    return getRegressionFor(x,y,xp)

if __name__ == "__main__":
    xp = np.linspace(13, 23, 11)
#    print guess(xp)
    print guess(0.03)
