#
# powerusage.py
#

import matplotlib.pyplot as plt
import csv

powerusage = []
dates = []

with open('powerusage.csv', 'r') as f:
    lines = f.readlines()

for line in lines:
    s_lines = line.strip().split(',')
    powerusage.append(int(s_lines[0]))
    dates.append(s_lines[1])

print("Power usage: ", powerusage)
print("Date: ", dates)


plt.plot(dates, powerusage)
plt.show()
