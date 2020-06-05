#
# usagecomparison.py - compares daily power usage to weather
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# reading in dataframes from csv files
weather_df = pd.read_csv('may_max.csv')  # first data frame is our weather, which is the daily maxmums 
power_df = pd.read_csv('powerusage.csv')

# appending date objects
weather_df['date'] = pd.to_datetime(weather_df['date'], format='%d-%m-%Y')
power_df['date'] = pd.to_datetime(power_df['date'], format='%d %m %Y')

# extracting dates from weather dataframe
weather_dates = weather_df['date']
# extracting daily maximums
weather_max = weather_df['max']

# extracting dates from power dataframe
power_dates = power_df['date']
# extracitng cumlative power usage
power_usage = power_df['usage']

# creating a new dataframe, which is how much power is used each day, instead of cumulative
difference_df = power_df['usage'].diff()

daily_dates = power_dates[:-1]            # had an extra day as it subtracts each element from the next day
daily_usage = difference_df[1:]          # element zero is a header so slice it out (exclude it) 
print(daily_usage.describe())


# we want to plot two values that have different y values but share x values
# - if we had the same y values the scale would be off

# first y axis
fig, ax1 = plt.subplots()
ax1.set_title("Daily Power Usage vs Weather")
ax1.set_xlabel("Date")
ax1.set_ylabel("Power Usage (kWh)")
ax1.bar(daily_dates, daily_usage, label="Power Usage", edgecolor='black') # plotting usage as a bar plot
plt.legend()

# second y axis
ax2 = ax1.twinx() # second axis that shares the same y axis
ax2.set_ylabel("Temp (c)")
ax2.plot(daily_dates, weather_max[:-3], 'y-', label="Maximum Temperature") # plotting weather as a yellow line
plt.legend() # showing legends

plt.show()
