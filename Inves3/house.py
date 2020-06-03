#
# house.py - create a house object
#
import csv
import numpy as np

class House():
    def __init__(self, address, housetype, postcode, numResidents, numBeds, numBaths, appliancefile):
        self.housetype = housetype
        self.address = address
        self.postcode = postcode
        self.numResidents = numResidents
        self.numBeds = numBeds
        self.numBaths = numBaths
        self.appliances = self.readAppliance(appliancefile) # list of appliances include name, wattage and a 24hr usage record

    def readAppliance(self, filename):
        appliancelist = []
        # importing the csv file
        with open(filename, newline='') as csvfile:
            # read each lines, delimeter is ':'
            reader = csv.reader(csvfile, delimiter=':') # seperate on ':'
            for row in reader:
                # append the whole row to the appliance list
                appliancelist.append(row)
        return appliancelist

    # just gets the names, which is the first element in each row
    def getApplianceNames(self):
        app = []
        for row in self.appliances:
            app.append(row[0])
        return app

    def getUsage(self):
        usage = []
        # looping through each appliance
        for row in self.appliances:           # for each element
            appliancewattage = float(row[1])  # assign wattage
            p_usage = row[2]                  # assign the usage record
            usagelist = [float(i) * appliancewattage for i in p_usage.split(',')] # eg// 200w * [0,1,0.5] = [0,200,100]
            # appending usage
            usage.append(usagelist)
        return usage

    def getNumResidents(self):
        return self.numResidents

    # the total usage of every appliance at each our in one array
    def calcTotalUsage(self):
        # adding elementwise each element in each array
        usage = self.getUsage()
        # converting each list in the list to a list of np.arrays
        npUsage = []
        for i in usage:
            npUsage.append(np.array(i))

        return sum(npUsage)

    # returns 24hr usage from given wattage and usage record
    def calcDailyUsage(self):
        usage = self.getUsage()

        # finds the sum total for the 24 hours
        total = 0.0
        for appliance in usage: #for each [xxx],[xxx]
            for element in appliance: # for each [(x)(x)(x)]
                total = total + element # adding each element
        return total

    # imports an integer value 'hour'
    def calcUsageAtTime(self, hour):
        usage = self.getUsage()

        # finds the sum total AT a given time (index)
        total = 0.0
        for element in usage:
            total = total + (element[hour])
        return total

    def printit(self):
        print("Address: " + self.address +  "\nPostcode: " + str(self.postcode) + "\nNumber of Residents: "  + str(self.numResidents) + "\nNumber of Beds: " + str(self.numBeds) + "\nNumber of Bathrooms: " + str(self.numBaths) + "\nAppliances: " + str(self.getApplianceNames()) + "\nTotal Power Usage (Watts/24hr): " + str(self.calcDailyUsage()))	

class Mansion(House):
    housetype = "Mansion"
    numResidents = 3
    numBeds = 8
    numBaths = 4
    appliancefile = "mansion.csv"

    def __init__(self, address, postcode):
        super().__init__(address, self.housetype, postcode, self.numResidents, self.numBeds, self.numBaths, self.appliancefile)

class Flat(House):
    housetype = "Flat"
    numResidents = 2
    numBeds = 2
    numBaths = 2
    appliancefile = "flat.csv"

    def __init__(self, address, postcode):
        super().__init__(address, self.housetype, postcode, self.numResidents, self.numBeds, self.numBaths, self.appliancefile)

class Family(House):
    housetype = "Family"
    numResidents = 4
    numBeds = 4
    numBaths = 2
    appliancefile = "family.csv"
        
    def __init__(self, address, postcode):
        super().__init__(address, self.housetype, postcode, self.numResidents, self.numBeds, self.numBaths, self.appliancefile)

class Studio(House):
    housetype = "Studio"
    numResidents = 1
    numBeds = 1
    numBaths = 1
    appliancefile = 'studio.csv'

    def __init__(self, address, postcode):
        super().__init__(address, self.housetype, postcode, self.numResidents, self.numBeds, self.numBaths, self.appliancefile)
