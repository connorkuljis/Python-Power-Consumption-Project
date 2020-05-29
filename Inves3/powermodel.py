import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

class powermodel:

    def sayHello():
        print("Say hello!")

    def calcUsage():
        appliance = []
        wattage = []
        usage = []
        everything = []
        times=range(1,25)

        # importing the csv file
        with open('myhouse.csv', newline='') as csvfile:
            modelreader = csv.reader(csvfile, delimiter=':') # seperate on ':'
            for row in modelreader:
                # the format follows; ['appliance name','wattage','power usage']
                # currently each row is stored as a String
                # going to split each element into separate lists and convert datatype if needed
           
                appliancenames = row[0]
                appliancewattage = float(row[1])
                p_usage = row[2]
                
                # appending appliance names
                appliance.append(appliancenames)
                
                # appending appliance wattage
                wattage.append(appliancewattage)
                               
                # list comprehension splitting the long string of numbers into floats and multiplying by current wattage
                usagelist = [float(i) * appliancewattage for i in p_usage.split(',')] 
                # appending usage
                usage.append(usagelist)

        return usage

    def readFile(filename):
        appliancelist = []

        # importing the csv file
        with open(filename, newline='') as csvfile:
            modelreader = csv.reader(csvfile, delimiter=':') # seperate on ':'
            for row in modelreader:
                appliancelist.append(row)

        return appliancelist

