#
# usage.py - creates subplots of powerusage and temperature
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# creating dataframes from csv file
weather_df = pd.read_csv('may_max.csv')
power_df = pd.read_csv('powerusage.csv')

# creating dateobjects using pandas
weather_df['date'] = pd.to_datetime(weather_df['date'], format='%d-%m-%Y')
power_df['date'] = pd.to_datetime(power_df['date'], format='%d %m %Y')

# creating lists for weather
weather_dates = weather_df['date']
weather_max = weather_df['max']

# creating lists for power
power_dates = power_df['date']
power_usage = power_df['usage']

# creating a new dataframe, which is how much power is used each day, instead of cumulative
difference_df = power_df['usage'].diff()

daily_dates = power_dates[:-1]            # slice to exclude last date as daily usage is one element shorter
daily_usage = difference_df[1:]          # element zero is a header so slice it out (exclude it)

# plotting temperature
plt.figure(1)
plt.subplot(221)      
plt.title("Perth Daily Maximums May 2020")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.plot(weather_dates, weather_max)

# plotting cumulative power usaeg
plt.subplot(212)                      
plt.title("Cumulative Power Usage")
plt.xlabel("Date")
plt.ylabel("Power Usage (kWh)")
plt.plot(power_dates, power_usage, 'r--')

# plotting daily power usage
plt.subplot(222)                          
plt.title("Daily Power Usage")
plt.xlabel("Date")
plt.ylabel("Power Usage (kWh)")
plt.plot(daily_dates, daily_usage, 'm-')

plt.show()








