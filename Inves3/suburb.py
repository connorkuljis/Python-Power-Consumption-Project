#
# suburb.py
#
from house import *
import numpy as np

class Suburb():
    def __init__(self, name, postcode):
        self.name = name
        self.postcode = postcode
        self.houses = []

    def displayHouses(self):
        print("Current Houses in Suburb: " + str(self.postcode))
        for house in self.houses:
            print(house.printit())
            print()

    def newHouse(self, houseType, address):
        temp = None
        if houseType == 'Mansion':
            temp = Mansion(address, self.postcode)
        elif houseType == "Flat":
            temp = Flat(address, self.postcode)
        elif houseType == "Family":
            temp = Family(address, self.postcode)
        elif houseType == "Studio":
            temp = Studio(address, self.postcode)
        else:
            print("Error processing house -> '" + houseType + "' (please double check values)")
        if temp:
            self.houses.append(temp)
            print("Added " + houseType + ": " + address + " to Suburb - " + self.name + " (" + str(self.postcode) + ")")

    def calcDailyUsage(self):
        total = 0.0
        for house in self.houses:
            total = total + house.calcDailyUsage()
        return total

    def calcUsageAtTime(self, hour):
        total = 0.0
        for house in self.houses:
            total = total = house.calcUsageAtTime(hour)
        return total

    def calcNumResidents(self):
        total = 0
        for house in self.houses:
            total = total + house.getNumResidents()
        return total

    def calcTotalUsage(self):
        npUsage = []
        for house in self.houses:
            npUsage.append(house.calcTotalUsage())

        return sum(npUsage)













