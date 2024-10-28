import numpy as np

data = np.loadtxt("/home/bene/Documents/Code/kik-epp1/Vorlesungen/28-10-24/data.csv", delimiter=",", skiprows=1)

x = data[ : ,0:2 ] # : -> von bis (exklusiv)
print (x)

y = x