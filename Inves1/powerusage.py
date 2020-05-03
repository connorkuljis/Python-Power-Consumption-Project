#
# powerusage.py
#

import numpy as np
import matplotlib.pyplot as plt
import csv

powerusage = []
dates = []

with open('powerusage.csv', 'r') as f:
    lines = f.readlines()

print(lines)
