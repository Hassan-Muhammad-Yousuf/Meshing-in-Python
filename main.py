import numpy as np
import matplotlib.pyplot as plt
import math

# creating Nodes 
left = 0.1
right = 0.02
height = 0.05

nb_elements = 10

# Nodes = np.array([[0,0],[0,1],[1,0],[1,1]]) (for testing purposes)
Nodes = []

for x in np.linspace(0, left , nb_elements):
    for y in np.linspace(0, height , nb_elements):
        Nodes.append([x,y])
 


#Displaying Nodes
points = np.array(Nodes)
plt.plot(points[:,0],points[:,1], 'o')

plt.show()

