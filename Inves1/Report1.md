# Investigation 1 Report - Power Usage

# Abstract
 The recording of power usage allows for the analysis of power usage trends and other underlying data that contributes to power usage. This paper explores the results of recording a power meter at a residence, by measuring the data approximately every 24 hours and documenting the results. Using python 3.7 and modules related to the anacoda distribution, a shallow analysis of power usage can be made. Python allows the power usage trends to be compared against other data sets, such as weather. Using the pandas module statistical data can be inferred.

# Background
Energy usage or power usage in homes are typically recorded on a power meter located on the premise. They are used to measure how much energy is consumed on the property. Power usage is stored in kilowatt-hours (kWh). Generally the trends of power usage can be correlated to internal or external factors upon the residents of the household. One relationship that will be explored is the relation between energy usage and maximum temperature for the day. This report makes uses of the pandas software library for python. The pandas package simply allows for data to be analysed and manipulated, in particular using a dataframe. A dataframe is tabular data structure that consists of rows and columns.

# Methodology
Each day at approximately 9:00pm the reading of the power meter will be documented in a CSV (Comma Separated Values) file, along side the current date. The recordings were taken for 20 days beginning on the 3rd of May. Once the data is recorded, the daily maximum temperatures for May 2020, Perth, Western Australia are downloaded from the Bereau of Meteorology (BoM) and stord in an adjacent CSV file. Using the pandas package the CSV files are parsed in and stored in a pandas data frame. The data is then further pulled apart and stored in labeled lists, including creating lists of date objects. As the readings from the power meter record cumulative power usage and not the day to day power usage, a new dataframe was created using the `.diff()` method which allows fo


# Results

# Conclusion and Future Work

# References
