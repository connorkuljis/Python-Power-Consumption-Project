#
# driver.py - driver code for creating house objects
#
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from house import *
from suburb import *


print("### CREATING SUBURB")
suburbname  = sys.argv[1] 
postcode = sys.argv[2]
testBurb = Suburb(suburbname, postcode)

# Mansion, Family, Flat, Studio
streetname = "Copper Street"
mm = int(sys.argv[3]) # number of mansions
ff = int(sys.argv[4]) # number of family houses
fl = int(sys.argv[5]) # number of flats
st = int(sys.argv[6]) # number of studios

for i in range(mm):
    testBurb.newHouse("Mansion", (str(i + 1) + " " + streetname))

for i in range(ff):
    testBurb.newHouse("Family", (str(mm + i + 1) + " " + streetname))

for i in range(fl):
    testBurb.newHouse("Flat", (str(mm + ff + i + 1) + " " + streetname))

for i in range(st):
    testBurb.newHouse("Studio", (str(mm + ff + fl  + i + 1) + " " + streetname))

print('### Calculating Power Usage ###')
daily_power_usage = testBurb.calcDailyUsage()
print("Daily Power Usage (Total) (w/hour): " + str(daily_power_usage))
print("Power Usage at Midday (w/hour): " + str(testBurb.calcUsageAtTime(12)))
numResidents = testBurb.calcNumResidents()
print("Number of Residents: " + str(numResidents))

avg = daily_power_usage / numResidents
print("Average daily power usage per resident: " + str(avg))

usage = testBurb.calcTotalUsage()
time = range(0,24)

plt.title(suburbname + " Daily Power Usage, Mansions = " + str(mm) + ", Familys  = " + str(ff) + ', Flats  = ' + str(fl) + ", Studios = " + str(st))
plt.xlabel("Time (in 24hr format)")
plt.ylabel("Energy Usage (W/hr)")
plt.plot(time, usage)
plt.savefig('HOUSE_MODEL' + 'MM' + str(mm) + '_FF' + str(ff) + "_FL" + str(fl) + "_ST" + str(st) + '.png')


#Dianella.newHouse("Mansion", "65 Applecross Road", 4)
#Dianella.newHouse("Flat", "1 Slate Street", 1)

# Dianella.calcDailyUsage()

#testBurb.displayHouses()


#print("## CONSTRUCTING HOUSE OBJECTS")
#h1 = House("65 Sattelberg Ramble", 6059, 4, 2, 4, 'myhouse.csv')
#h1.printit()
#hour = 23
#h1.calcUsageAtTime(hour)

#mcMansion = Mansion("abcd", 1000, 2)
#mcMansion.printit()
#
#small = Flat("1 aberdeen st", 2000, 2)
#small.printit()
#
#nuclear = Family("1 infinite loop", 4503, 4)
#nuclear.printit()
#
#stu = Studio("1 new yorker", 54, 1)
#stu.printit()




