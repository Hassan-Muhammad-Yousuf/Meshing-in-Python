import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import Delaunay  

# creating Nodes 
left = 0.1
right = 0.02
height = 0.05

nb_elements = 20

# Nodes = np.array([[0,0],[0,1],[1,0],[1,1]]) (for testing purposes)
Nodes = []

for x in np.linspace(0, left , nb_elements):
    if x < right:
        y0 = math.sqrt(right**2 - x**2)
        for y in np.linspace(y0, height , nb_elements):
            Nodes.append([x,y])

    else:
        for y in np.linspace(0, height , nb_elements):
            Nodes.append([x,y])
 


#Displaying Nodes
points = np.array(Nodes)
plt.plot(points[:,0],points[:,1], 'o')



# Creating Elements
tr1 = Delaunay(points)
plt.triplot(points[:,0],points[:,1], tr1.simplices)
plt.plot(points[:,0],points[:,1], 'o')

#plt.show()

#creating a set of points on a circle diameter
p = []
r2 = 0.0195
for x in np.linspace(0, r2, 10):
    p.append([x,math.sqrt(r2**2-x**2)])

#find the points which contain those elements
print(tr1.find_simplex(p))

#creating the new set of elements without disturbing circle


