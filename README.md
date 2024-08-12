# Mesh Generation and Visualisation.

This project creates a finite element mesh for a geometric domain and then visualises it using Delaunay triangulation. It also contains the ability to export mesh data to a text file.

## Overview.

The code carries out the following tasks:

1. **Node Generation**: Generates nodes for a given geometric domain by joining a semicircle and a rectangle.
2. **Delaunay Triangulation**: A mesh is generated using Delaunay triangulation based on the nodes.
3. **Circle Points Identification**: Determines whether mesh elements include certain points on a circle.
4. **Mesh Modification**: Shows how to edit the mesh by eliminating certain elements.
5. **Visualisation**: Plots the nodes and mesh with'matplotlib'.
6. **Data Export**: Saves node and mesh data to a text file.

## Requirements

Python 3.x, NumPy, Matplotlib, and SciPy



