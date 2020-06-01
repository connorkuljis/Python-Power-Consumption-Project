#
# driver.py - driver code for creating house objects
#
import sys
import matplotlib.pyplot as plt
from house import *
from suburb import *


print("### CREATING SUBURB")
suburbname  = 'Dianella'
postcode = 4444
testBurb = Suburb(suburbname, postcode)

# Mansion, Family, Flat, Studio
streetname = "Copper Street"
mm = 2
ff = 4
fl = 5
st = 10

for i in range(mm):
    testBurb.newHouse("Mansion", (str(i + 1) + " " + streetname))

for i in range(ff):
    testBurb.newHouse("Family", (str(mm + i + 1) + " " + streetname))

for i in range(fl):
    testBurb.newHouse("Flat", (str(mm + ff + i + 1) + " " + streetname))

for i in range(st):
    testBurb.newHouse("Studio", (str(mm + ff + fl  + i + 1) + " " + streetname))

print('### Calculating Power Usage ###')
print(testBurb.calcDailyUsage())
print(testBurb.calcUsageAtTime(4))
print(testBurb.calcNumResidents())

usage = testBurb.calcTotalUsage()
time = range(0,24)

plt.title(suburbname + " Daily Power Usage, Mansions = " + str(mm) + ", Familys  = " + str(ff) + ', Flats  = ' + str(fl) + ", Studios = " + str(st))
plt.plot(time, usage)
plt.show()




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




