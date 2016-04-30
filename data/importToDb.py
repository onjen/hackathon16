import csv
import sqlite3
import datetime
import time

 
conn = sqlite3.connect('data.db')
for i in xrange(1, 6): 
    with open('Anlage' + str(i) + '.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if reader.line_num == 1:
                continue
            date = int(time.mktime(time.strptime(row[0], "%Y-%m-%d %H:%M:%S")))
            outdoor = float(row[1])
            target = float(row[2])
            kwh = float(row[3])

            conn.execute("INSERT INTO DATA (TIME, OUTDOOR, TARGET, ENERGY) VALUES (" + str(date) + "," + str(outdoor) + "," + str(target) + "," + str(kwh) + ")");

conn.commit()
conn.close()
