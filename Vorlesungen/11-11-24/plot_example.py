import matplotlib.pyplot as plt 
import numpy as np 


#fig = plt.figure()

np.random.seed(435982)
n = 100

rng =  np.random.default_rng()
xs = rng.uniform(23,32,n)
ys = rng.uniform(0,100,n)
zs = rng.uniform(-50,-25,n)



fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.scatter(xs,ys,zs, s=100)
ax.set(xticklabels=[10,20,30,40,50],
       yticklabels =[10,20,30,40,50,100],
       zticklabels =[10,20,30,40,50,100])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
#ax.set_autoscale_on
ax.set_title("kein kuchen")
#plt.figure()

plt.show()