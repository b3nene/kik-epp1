import numpy as np

data = np.loadtxt("/home/bene/Documents/Code/kik-epp1/Vorlesungen/28-10-24/data.csv", delimiter=",", skiprows=1)

x = data[ : ,0:3 ] # : -> von bis (exklusiv)
#print (x)

y = data[: , 2]

#print (y)

for i in range(x.shape[0]):
    print ("Datapoint: ",i)
    print("A,H,OS",data[i])
    print("age: ", x[i,0])
    print("height:", x[i,1])
    if x[i,2]==0:
        print ("android")
    else:
        print("iOs")
    