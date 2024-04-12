# A basic plotter for a file containing photodiode data

import pandas
import matplotlib

filename = 'Data/S47_data_out_7.csv'

# Read the data
data = pandas.read_csv(filename)

# Plot the data
data.plot(x=1, y=3)
data.plot(x=1, y=4)
data.plot(x=1, y=5)
data.plot(x=1, y=6)

# Show the plot
matplotlib.pyplot.show()