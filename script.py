# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(flights, range = (0, 365), bins = 365, edgecolor = "black")
plt.title("Traveling to Acadia")
plt.xlabel("Day of The Year")
plt.ylabel("Flight Count")

plt.subplot(212)
plt.hist(in_bloom, range = (0,365), bins = 365, edgecolor = "black")
plt.title("Flower Blooms and Flights by Day")
plt.xlabel("Day of The Year")
plt.ylabel("Bloom Count")

plt.show()