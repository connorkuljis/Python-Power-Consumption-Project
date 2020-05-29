#
# house.py - create a house object
#
import csv

class House():
    def __init__(self, address, postcode, numResidents, numBeds, numBaths, appliancefile):
        self.address = address
        self.postcode = postcode
        self.numResidents = numResidents
        self.numBeds = numBeds
        self.numBaths = numBaths
        self.appliances = self.readFile(appliancefile)

    def getApplianceNames(self):
        app = []
        for row in self.appliances:
            app.append(row[0])
        return app

    def readFile(self, filename):
        appliancelist = []

        # importing the csv file
        with open(filename, newline='') as csvfile:
            modelreader = csv.reader(csvfile, delimiter=':') # seperate on ':'
            for row in modelreader:
                appliancelist.append(row)

        return appliancelist

    def calcUsage(self):
        usage = []
        for row in self.appliances:
            appliancewattage = float(row[1])
            p_usage = row[2]
            usagelist = [float(i) * appliancewattage for i in p_usage.split(',')] 
            # appending usage
            usage.append(usagelist)

        total = 0.0
        for appliance in usage:
            for element in appliance:
                total = total + element

        return total

    def printit(self):
        print("Address: " + self.address +  "\nPostcode: " + str(self.postcode) + "\nNumber of Residents: " + str(self.numResidents) + "\nAppliances: " + str(self.getApplianceNames()) + "\nTotal Power Usage (Watts/24hr): " + str(self.calcUsage()))

class Mansion(House):
    numBeds = 5
    numBaths = 4
    appliancefile = "mansion.csv"

    # on a right track here
    def __init__(self, address, postcode, numResidents):
        super().__init__(address, postcode, numResidents, self.numBeds, self.numBaths, self.appliancefile)

class Flat(House):
    pass


        

