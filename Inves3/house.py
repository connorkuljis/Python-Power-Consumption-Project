#
# house.py
#
# comments: the list of appliances should be static and can each house type can provide a string list of the appliances 

# --HOUSE SUPERCLASS
class House():
    myclass = "House"

    def __init__(self, numBedrooms, numBathrooms, appliance, hasSolar):
        self.numBedrooms = numBedrooms
        self.numBathrooms = numBathrooms
        self.appliance = appliance # could be a list of applicances
        self.hasSolar == hasSolar

    def calcEnergyOutput(self):
        pass

## --HOUSE SUBCLASSES
class HouseA(House):
    myclass = "HouseA"
    
    numBedrooms = 4
    numBathrooms = 2
    appliance = 

    def __init__(self):
        House.__init__(self,)

    pass

class HouseB(House):
    myclass = "HouseB"

    pass

class HouseC(House):
    myclass = "HouseC"

    pass

class HouseD(House):
    myclass = "HouseD"

    pass

# --SUBURB CLASS
# can make a suburb out of a list of house objects
# IMPORTS: name, postcode, houses (ARRAY OF House Objects)

class Suburb(self, name, postcode, houses):
    self.name = name
    self.postcode = postcode
    self.houses = houses

    def calcOutput(self):
        pass








# aircon will be used less in winter
# weekday vs weekend


