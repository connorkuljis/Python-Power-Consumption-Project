#
# newpd.py -
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

weather_df = pd.read_csv('may_max.csv')  # first data frame is our weather, which is the daily maxmums 
power_df = pd.read_csv('powerusage.csv')

weather_df['date'] = pd.to_datetime(weather_df['date'], format='%d-%m-%Y')
power_df['date'] = pd.to_datetime(power_df['date'], format='%d %m %Y')

weather_dates = weather_df['date']
weather_max = weather_df['max']

power_dates = power_df['date']
power_usage = power_df['usage']

difference_df = power_df['usage'].diff()
daily_dates = power_dates[:-1]            # slice to exclude last date as daily usage is one element shorter
daily_usage = difference_df[:-1]          # becuase the diff_df has no label use slicing to get last element

# first y axis
fig, ax1 = plt.subplots()
ax1.set_title("Daily Power Usage vs Daily Maximums")
ax1.set_xlabel("Date")
ax1.set_ylabel("Power Usage (kWh)")
ax1.bar(daily_dates, daily_usage, label="Power Usage", edgecolor='black')
plt.legend()

# second y axis
ax2 = ax1.twinx() # second axis that shares the same y axis
ax2.set_ylabel("Temp (c)")
ax2.plot(daily_dates, weather_max[:-3], 'y-', label="Maximum Temperature")
plt.legend()

plt.show()
