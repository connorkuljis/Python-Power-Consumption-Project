#
# newpd.py -
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

weather_df = pd.read_csv('may_max.csv')
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

plt.figure(1)
plt.subplot(221)                          # temperature
plt.title("Perth Daily Maximums May 2020")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.plot(weather_dates, weather_max)

plt.subplot(212)                          # cumulative power
plt.title("Cumulative Power Usage")
plt.xlabel("Date")
plt.ylabel("Power Usage (kWh)")
plt.plot(power_dates, power_usage, 'r--')

plt.subplot(222)                          # daily power
plt.title("Daily Power Usage")
plt.xlabel("Date")
plt.ylabel("Power Usage (kWh)")
plt.plot(daily_dates, daily_usage, 'm-')

plt.show()








