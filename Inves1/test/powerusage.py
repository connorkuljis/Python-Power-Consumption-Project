#
# powerusage.py
#

import matplotlib.pyplot as plt
import pandas as pd
import csv

powerusage = []
dates = []

with open('powerusage.csv', 'r') as f:
    lines = f.readlines()

# cleaning csv and sorting into lists
for line in lines:
    s_lines = line.strip().split(',')
    powerusage.append(int(s_lines[0]))
    dates.append(s_lines[1])

# just get the daily change
# doing this creates a list that is the length of powerusage - 1
dailyusage = [j - i for i, j in zip(powerusage[: -1], powerusage[1 :])]

print("Daily usage:", dailyusage)
print("Power usage: ", powerusage)
print("Date: ", dates)

plt.figure(1)
plt.subplot(211)
plt.title("Cumulative Power Usage Over Time")
plt.xlabel("Date")
plt.ylabel("Energy Usage (kWh)")
plt.plot(dates, powerusage, 'r-')

plt.subplot(212)
plt.title("Daily Power Usage Over Time")
plt.xlabel("Date")
plt.ylabel("Energy Usage (kWh)")
# accounting for the length of daily usage being len(powerusage) - 1, by slicing the dates
plt.plot(dates[1:], dailyusage, 'b--')

plt.show()
