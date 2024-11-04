

shapes = ["square", "circle", "triangle"]

shapes[2]= "hexagon"

print(shapes)

tupleshape = ("square","circle","pentagon")

print(tupleshape)

shape_parameters = {
    "square": 1.0,
    "circle": 3.5,
    "triangle": (2.0,3.0,42)
}

print(shape_parameters)
print(shape_parameters["circle"])

import numpy as np

start_value = 0
end_value = 50
step = 1.75

# Festgelegter Abstand step
values = np.arange(start_value,end_value,step)
print(values)

#Festgelegte Zwischenschritte n
n = 13
othervals = np.linspace(start_value,end_value, n) 
print(othervals)

import pandas as pd 

df = pd.DataFrame({
    'Feature A': [1,2,8],
    'Feature B': [2,5,8]
})

print(df)