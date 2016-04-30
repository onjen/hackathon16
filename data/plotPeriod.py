import csv
import matplotlib.pyplot as plt
import sqlite3
import datetime

# column: TIME, OUTDOOR, TARGET, ENERGY
def readColumnFromDB(column):
    data = []
    conn = sqlite3.connect('data.db')
    cursor = conn.execute('SELECT %s FROM DATA' % (column,) )
    for row in cursor:
        data.append(row[0])
    conn.close()
    return data

def getPeriod(start_stamp, end_stamp, column):
    data = []
    conn = sqlite3.connect('data.db')
    cursor = conn.execute('SELECT %s FROM DATA WHERE TIME > %s AND TIME < %s '%\
            (column,start_stamp,end_stamp,))
    for row in cursor:
        data.append(row[0])
    conn.close()
    return data

def main():
    column = 'OUTDOOR'
    data = getPeriod(1450398780,1450407810,column);
    plt.plot(data)
    plt.xlabel('30sec steps')
    plt.ylabel(column)
    plt.show()

if __name__ == "__main__":
        main()
