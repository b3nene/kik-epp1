import numpy as np
import sklearn.tree
from sklearn.tree import plot_tree

data = np.loadtxt("/home/bene/Documents/Code/kik-epp1/Vorlesungen/28-10-24/data.csv", delimiter=",", skiprows=1)

x = data[ : ,0:2] # : -> von bis (exklusiv)
#print (x)

y = data[: , 2]

#print (y)

#for i in range(x.shape[0]):
 #   print ("Datapoint: ",i)
  #  print("A,H,OS",data[i])
   # print("age: ", x[i,0])
    #print("height:", x[i,1])
    #if y[i,2]==0:
     #   print ("android")
    #else:
     #   print("iOs")
    
decision_tree = sklearn.tree.DecisionTreeClassifier(criterion="gini")
decision_tree.fit(x,y)

prediction = [36, 176]
nppred = np.array(prediction)
rnppred= nppred.reshape(1, -1)

print(
    decision_tree.predict(rnppred)
)